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
        default_vars = host.ansible("include_vars", "../../roles/certificates/defaults/main.yml")["ansible_facts"]
        value = default_vars[name]

    return value


def test_pkg(host):
    package_name = get_variable(host, "certificates_ca_package_name")
    assert package_name != ""

    package = host.package(package_name)
    assert package.is_installed


def test_files(host):
    certificates = get_variable(host, 'certificates_ca')
    path = get_variable(host, 'certificates_ca_path')

    assert type(certificates) is list
    assert path != ""

    for ca_cert in certificates:
        file = host.file(f"{path}/{ca_cert['name']}")
        assert file.exists
        assert file.user == "root"
        assert file.group == "root"
        assert file.mode == 0o644
