import pytest

from ..util.util import (
    get_ansible,
    get_variable,
    get_family_role_variable,
    jinja_list_concat,
)

testinfra_runner, testinfra_hosts = get_ansible()


def test_cleanup_service(host):
    services = get_variable(host, "cleanup_services")
    services_default = get_variable(host, "cleanup_services_default")
    services_extra = get_variable(host, "cleanup_services_extra")

    services_distribution = get_family_role_variable(
        host, "__cleanup_services_distribution"
    )

    services = jinja_list_concat(
        services, [services_default, services_extra, services_distribution]
    )

    for service_name in services:
        service = host.service(service_name)

        # service.exists is not working because of:
        # b'systemctl list-unit-files | grep -q"^ModemManager.service"', _stdout=b'',
        # _stderr=b"grep: invalid option -- '^'\nUsage: grep [OPTION]... PATTERNS [FILE]...\n
        # Try 'grep --help' for more information.\n"
        cmd = host.run(
            f'systemctl list-units --all | grep -q "^[[:space:]]*{service_name}"'
        )

        if cmd.rc == 0:
            assert not service.is_enabled, f"{service_name} should not be enabled"
            assert not service.is_running, f"{service_name} should not be running"
        else:
            pytest.skip(f"The {service_name} service does not exist")
