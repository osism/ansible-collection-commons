# Your existing imports and setup code
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
        default_vars = host.ansible("include_vars", "../../roles/facts/defaults/main.yml")["ansible_facts"]
        value = default_vars[name]
    return value


def test_custom_facts_directory(host):
    facts_dir = host.file('/etc/ansible/facts.d')

    assert facts_dir.exists
    assert facts_dir.is_directory
    assert facts_dir.user == "root"
    assert facts_dir.group == "root"
    assert facts_dir.mode == 0o755


def test_fact_files(host):
    fact_files = get_variable(host, 'fact_files')

    assert type(fact_files) is list

    for fact_file in fact_files:
        file = host.file(f'/etc/ansible/facts.d/{fact_file}.fact')

        assert file.exists
        assert file.user == "root"
        assert file.group == "root"
        assert file.mode == 0o755
