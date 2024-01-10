from .util.util import get_ansible, get_variable, jinja_replacement

testinfra_runner, testinfra_hosts = get_ansible()


def test_known_hosts_file_permissions(host):
    operator_user = get_variable(host, "operator_user")
    operator_group = get_variable(host, "operator_group")

    known_hosts_destination = get_variable(host, "known_hosts_destination")
    known_hosts_destination = jinja_replacement(
        known_hosts_destination, {"operator_user": operator_user}
    )
    known_hosts_destination += "/known_hosts"

    f = host.file(known_hosts_destination)

    assert f.exists, f"The known_hosts file does not exist: {known_hosts_destination}"
    assert not f.is_directory
    assert (
        f.user == operator_user
    ), f"The known_hosts file is not owned by {operator_user}"
    assert (
        f.group == operator_group
    ), f"The known_hosts file is not grouped by {operator_group}"
    assert f.mode == 0o600, "The known_hosts file does not have 0600 permissions"


def test_known_hosts_file_content(host):
    operator_user = get_variable(host, "operator_user")

    known_hosts_destination = get_variable(host, "known_hosts_destination")
    known_hosts_destination = jinja_replacement(
        known_hosts_destination, {"operator_user": operator_user}
    )
    known_hosts_destination += "/known_hosts"

    f = host.file(known_hosts_destination)

    known_hosts_list = get_variable(host, "known_hosts_list")
    for expected_host in known_hosts_list:
        # Each line in the known_hosts file should contain the expected host.
        assert f.contains(
            expected_host
        ), f"Host {expected_host} not found in {known_hosts_destination}"
