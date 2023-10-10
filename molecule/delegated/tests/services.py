import os
import pytest
import testinfra.utils.ansible_runner

testinfra_runner = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
)
testinfra_hosts = testinfra_runner.get_hosts('all')
services_warning_default = ["nscd"]
services_warning_extra = []
services_warning = services_warning_default + services_warning_extra
services_required_default = ["cron"]
services_required_extra = []
services_required = services_required_default + services_required_extra


def test_warning_services(host):
    for service_name in services_warning:
        service = host.service(service_name)
        assert not service.is_running, f"The {service_name} service is running. It should be deactivated and not run."
        assert not service.is_enabled, f"The {service_name} service is enabled. It should be deactivated and not run."


def test_required_services(host):
    for service_name in services_required:
        service = host.service(service_name)
        assert service.is_running, f"The {service_name} service is not running. It should be active and running."
        assert service.is_enabled, f"The {service_name} service is not enabled. It should be enabled."
