import os
import pytest
import testinfra.utils.ansible_runner

testinfra_runner = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE'])
testinfra_hosts = testinfra_runner.get_hosts('all')


def get_variable(host, name):
    result = host.ansible('debug', f'var={name}', check=False)
    value = result.get(name, None)
    if value is None or value.startswith('VARIABLE IS NOT DEFINED!'):
        default_vars = host.ansible("include_vars", "../../roles/sysctl/defaults/main.yml")["ansible_facts"]
        value = default_vars.get(name, None)
    return value


def test_sysctl_settings(host):
    group_names = host.ansible.get_variables().get('group_names', [])
    sysctl_defaults = get_variable(host, 'sysctl_defaults')
    sysctl_extra = get_variable(host, 'sysctl_extra')

    sysctl_config = sysctl_defaults.copy()
    sysctl_config.update(sysctl_extra)

    for group in group_names:
        settings = sysctl_config.get(group, [])
        for setting in settings:
            sysctl_name = setting['name']
            expected_value = str(setting['value'])
            sysctl_path = f"/proc/sys/{sysctl_name.replace('.', '/')}"

            if host.file(sysctl_path).exists:
                actual_value = host.file(sysctl_path).content_string.strip()
                assert actual_value == expected_value, f"Sysctl setting {sysctl_name} is {actual_value}, expected {expected_value}"
