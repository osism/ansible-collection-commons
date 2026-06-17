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


def test_preserved_file_keeps_local_ownership(host):
    # The restore must reapply the file's original owner, group and mode rather
    # than silently rewriting the secret to the user running the update (root
    # under become: true). The fixture creates it as operator_user:operator_group
    # with mode 0640.
    directory = get_variable(host, "configuration_directory")
    operator_user = get_variable(host, "operator_user")
    operator_group = get_variable(host, "operator_group")

    f = host.file(f"{directory}/netbox/settings.toml")

    assert f.user == operator_user
    assert f.group == operator_group
    assert f.mode == 0o640


def test_non_preserved_file_is_reset(host):
    # Control: marker.txt is tracked but not preserved, so the force checkout
    # must reset it to the repository version. This proves the checkout actually
    # ran and that the preservation is selective rather than a global no-op.
    directory = get_variable(host, "configuration_directory")

    content = read_file(host, f"{directory}/marker.txt")

    assert content.strip() == "FROM-REPOSITORY"


def test_no_preserve_backup_left_behind(host):
    # The run-scoped backup directory created around the force checkout must be
    # removed again afterwards, leaving no copy of the preserved secret behind —
    # neither inside the worktree nor in the system temp directory.
    directory = get_variable(host, "configuration_directory")

    stray_in_worktree = host.check_output(
        f"find {directory} -name '*.osism-preserve' -print -quit"
    )
    assert stray_in_worktree == ""

    stray_in_tmp = host.check_output(
        "find /tmp -maxdepth 1 -name 'osism-configuration-preserve.*' -print -quit"
    )
    assert stray_in_tmp == ""
