import os
import pytest
from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


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
