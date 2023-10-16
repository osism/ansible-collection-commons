import os
import pytest
from .util.util import get_ansible

testinfra_runner, testinfra_hosts = get_ansible()


def get_variable(host, name, role_path='packages', default=None):
    result = host.ansible('debug', f'var={name}')
    value = result.get(name, "VARIABLE IS NOT DEFINED!")

    if "VARIABLE IS NOT DEFINED!" in value:
        default_vars = host.ansible("include_vars", f"../../roles/{role_path}/defaults/main.yml")["ansible_facts"]
        value = default_vars.get(name, default if default is not None else "VARIABLE IS NOT DEFINED!")

    return value


def test_required_packages_installed(host):
    required_packages_default = get_variable(host, 'required_packages_default', default=[])
    required_packages_extra = get_variable(host, 'required_packages_extra', default=[])

    os_family = host.ansible("setup")["ansible_facts"]["ansible_os_family"]

    distribution_var_name = None
    if os_family == "Debian":
        distribution_var_name = "required_packages_debian"
    elif os_family == "RedHat":
        distribution_var_name = "required_packages_redhat"

    required_packages_distribution = []
    if distribution_var_name:
        required_packages_distribution = get_variable(host, distribution_var_name, default=[])

    all_required_packages = required_packages_default + required_packages_extra + required_packages_distribution

    for package_name in all_required_packages:
        package = host.package(package_name)
        assert package.is_installed, f"{package_name} is not installed"


@pytest.mark.parametrize("package_name", ["ethtool", "jq", "rsyslog"])
def test_default_packages_installed(host, package_name):
    package = host.package(package_name)
    assert package.is_installed


def test_package_upgrade(host):
    upgrade_packages = get_variable(host, 'upgrade_packages', 'packages')
    os_family = host.ansible("setup")["ansible_facts"]["ansible_os_family"]

    if upgrade_packages:
        if os_family == "Debian":
            upgradable = host.check_output('apt list --upgradable 2>/dev/null | wc -l')
            num_upgradable = int(upgradable.strip()) - 1  # subtract 1 to account for the header line
            print(f"There are {num_upgradable} packages that can be upgraded.")

        elif os_family == "RedHat":
            upgradable = host.check_output('dnf list upgrades --quiet | wc -l')
            num_upgradable = int(upgradable.strip())
            print(f"There are {num_upgradable} packages that can be upgraded.")
