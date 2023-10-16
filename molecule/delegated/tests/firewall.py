import os
import pytest
from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()

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
