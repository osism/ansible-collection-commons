import os
import pytest
import testinfra.utils.ansible_runner

testinfra_runner = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE'])
testinfra_hosts = testinfra_runner.get_hosts('all')


def get_variable(host, name):
    result = host.ansible('debug', f'var={name}')
    value = result[name]
    if value.startswith('VARIABLE IS NOT DEFINED!'):
        default_vars = host.ansible("include_vars", "../../roles/microcode/defaults/main.yml")["ansible_facts"]
        value = default_vars[name]

    return value


def test_microcode_packages(host):
    microcode_packages_default = get_variable(host, 'microcode_packages_default')
    microcode_packages_extra = get_variable(host, 'microcode_packages_extra')

    assert type(microcode_packages_default) is list
    assert type(microcode_packages_extra) is list

    microcode_packages = microcode_packages_default + microcode_packages_extra
    assert len(microcode_packages) > 0

    for package_name in microcode_packages:
        package = host.package(package_name)
        assert package.is_installed
