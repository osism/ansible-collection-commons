from ..util.util import (
    get_ansible,
    get_variable,
    get_os_role_variable,
    jinja_list_concat,
)

testinfra_runner, testinfra_hosts = get_ansible()


def test_cleanup_service(host):
    services = get_variable(host, "cleanup_services")
    services_default = get_variable(host, "cleanup_services_default")
    services_extra = get_variable(host, "cleanup_services_extra")

    services_distribution = get_os_role_variable(host, "cleanup_services_distribution")

    services = jinja_list_concat(
        services, [services_default, services_extra, services_distribution]
    )

    for service_name in services:
        service = host.service(service_name)
        assert not service.is_enabled
        assert not service.is_running
