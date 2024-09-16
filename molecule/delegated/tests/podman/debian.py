import pytest

from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "Debian":
        pytest.skip("ansible_os_family mismatch")


def test_uidmap_pkg(host):
    check_ansible_os_family(host)

    package_name = "uidmap"
    package = host.package(package_name)
    assert package.is_installed
