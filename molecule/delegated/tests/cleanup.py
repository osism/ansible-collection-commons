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


def test_path():
    assert not os.path.exists("/etc/cloud")


def test_srv(host):
    service_default = get_variable(host, "cleanup_services_default")
    service_extra = get_variable(host, "cleanup_services_extra")
    assert type(service_default) is list
    assert type(service_extra) is list

    for service in service_default and service_extra:
        assert not service.is_running


def test_pkg(host):
    package_default = get_variable(host, "cleanup_packages_default")
    package_extra = get_variable(host, "cleanup_packages_extra")
    assert type(package_default) is list
    assert type(package_extra) is list

    for package in package_default and package_extra:
        assert not package.is_running
