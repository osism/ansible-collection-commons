import pytest

from ..util.util import get_ansible, get_variable, get_family_role_variable

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "Debian":
        pytest.skip("ansible_os_family mismatch")


def test_dropbear_packages(host):
    check_ansible_os_family(host)

    dropbear_packages = get_family_role_variable(host, "dropbear_packages")

    for package_name in dropbear_packages:
        package = host.package(package_name)
        assert not package.is_installed
