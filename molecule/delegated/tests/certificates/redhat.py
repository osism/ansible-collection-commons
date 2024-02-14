import pytest

from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "RedHat":
        pytest.skip("ansible_os_family mismatch")


def test_pkg(host):
    check_ansible_os_family(host)

    package_name = get_variable(host, "certificates_ca_package_name")
    assert package_name != ""

    package = host.package(package_name)
    assert package.is_installed
