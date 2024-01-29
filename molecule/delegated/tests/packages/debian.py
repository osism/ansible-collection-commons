import pytest

from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "Debian":
        pytest.skip("ansible_os_family mismatch")


def test_package_upgrade(host):
    check_ansible_os_family(host)

    upgrade_packages = get_variable(host, "packages_upgrade")

    if not upgrade_packages:
        pytest.skip("packages_upgrade is not True")

    upgradable = host.check_output("apt list --upgradable 2>/dev/null | wc -l")
    # subtract 1 to account for the header line
    num_upgradable = int(upgradable.strip()) - 1
    assert num_upgradable == 0
