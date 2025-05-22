import pytest

from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "RedHat":
        pytest.skip("ansible_os_family mismatch")


def test_motd_files_exist(host):
    check_ansible_os_family(host)

    motd_path = get_variable(host, "motd_path")
    issue_path = get_variable(host, "issue_path")
    issue_net_path = get_variable(host, "issue_net_path")

    assert host.file(motd_path).exists
    assert host.file(issue_path).exists
    assert host.file(issue_net_path).exists
