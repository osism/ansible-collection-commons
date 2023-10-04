import os
import pytest
import testinfra.utils.ansible_runner

testinfra_runner = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE'])
testinfra_hosts = testinfra_runner.get_hosts('all')


def test_srv(host):
    service = host.service("sys-kernel-config.mount")

    assert service.is_running
    assert service.is_enabled
