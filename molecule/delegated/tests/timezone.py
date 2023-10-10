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
        default_vars = host.ansible("include_vars", "../../roles/timezone/defaults/main.yml")["ansible_facts"]
        value = default_vars.get(name, "VARIABLE IS NOT DEFINED!")

    return value


def test_tzdata_package(host):
    package = host.package('tzdata')
    assert package.is_installed


def test_timezone_settings(host):
    timezone_name = get_variable(host, 'timezone_name')
    timezone_hwclock = get_variable(host, 'timezone_hwclock')

    timezone_file = host.file('/etc/timezone')
    assert timezone_file.exists
    assert timezone_file.content_string.strip() == timezone_name

    hwclock_file = host.file('/etc/adjtime')
    if hwclock_file.exists:
        assert timezone_hwclock in hwclock_file.content_string
