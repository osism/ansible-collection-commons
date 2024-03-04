import pytest

from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "Debian":
        pytest.skip("ansible_os_family mismatch")


def test_pkg(host):
    check_ansible_os_family(host)
    assert not host.package("update-motd").is_installed

    # There isn't a direct equivalent to the "update-motd" package on CentOS.
