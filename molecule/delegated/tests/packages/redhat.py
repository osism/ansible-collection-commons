import pytest

from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "RedHat":
        pytest.skip("ansible_os_family mismatch")


def test_package_upgrade(host):
    check_ansible_os_family(host)

    upgrade_packages = get_variable(host, 'upgrade_packages')

    if not upgrade_packages:
        pytest.skip("upgrade_packages is not True")

    upgradable = host.check_output('dnf list upgrades --quiet | wc -l')
    num_upgradable = int(upgradable.strip())
    assert num_upgradable == 0
