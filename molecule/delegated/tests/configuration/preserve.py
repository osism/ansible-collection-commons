from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def read_file(host, path):
    user = get_variable(host, "operator_user")
    with host.sudo(user):
        return host.check_output(f"cat {path}")


def test_preserved_file_survives_update(host):
    # netbox/settings.toml is listed in configuration_git_preserve_files, so its
    # locally customized content must survive the force checkout instead of being
    # reset to the version tracked in the repository.
    directory = get_variable(host, "configuration_directory")

    content = read_file(host, f"{directory}/netbox/settings.toml")

    assert "LOCAL-SECRET-TOKEN" in content
    assert "FROM-REPOSITORY" not in content


def test_non_preserved_file_is_reset(host):
    # Control: marker.txt is tracked but not preserved, so the force checkout
    # must reset it to the repository version. This proves the checkout actually
    # ran and that the preservation is selective rather than a global no-op.
    directory = get_variable(host, "configuration_directory")

    content = read_file(host, f"{directory}/marker.txt")

    assert content.strip() == "FROM-REPOSITORY"


def test_no_preserve_backup_left_behind(host):
    # The backup created around the checkout must be removed again afterwards.
    directory = get_variable(host, "configuration_directory")

    backup = host.file(f"{directory}/netbox/settings.toml.osism-preserve")

    assert not backup.exists
