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
        default_vars = host.ansible("include_vars", "../../roles/cleanup/defaults/main.yml")["ansible_facts"]
        value = default_vars[name]

    return value


def test_hostname_settings(host):
    # Retrieve the hostname_name variable from Ansible
    hostname_name = get_variable(host, "hostname_name")

    # Verify that the hostname is correctly set
    assert hostname_name == host.check_output('hostname')

    # Verify the /etc/hostname file
    etc_hostname = host.file('/etc/hostname')
    assert etc_hostname.exists
    assert etc_hostname.content_string.strip() == hostname_name
    assert etc_hostname.user == 'root'
    assert etc_hostname.group == 'root'
    assert oct(etc_hostname.mode) == '0o644'
