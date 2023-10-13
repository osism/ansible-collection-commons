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
        default_vars = host.ansible("include_vars", "../../roles/firewall/defaults/main.yml")["ansible_facts"]
        value = default_vars[name]
    return value


def test_firewall_config_file(host):
    service_name = get_variable(host, 'ufw_service_name')
    file = host.file(f'/etc/ufw/{service_name}.conf')

    assert file.exists
    assert file.mode == 0o644


def test_firewall_service(host):
    service_name = get_variable(host, 'ufw_service_name')
    service = host.service(service_name)

    assert service.is_running
    assert service.is_enabled
