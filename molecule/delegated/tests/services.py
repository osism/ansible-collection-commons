from .util.util import get_ansible, get_variable, jinja_list_concat

testinfra_runner, testinfra_hosts = get_ansible()


def test_required_services(host):
    services_required = get_variable(host, "services_required")
    services_required_default = get_variable(host, "services_required_default")
    services_required_extra = get_variable(host, "services_required_extra")

    services_required = jinja_list_concat(
        services_required, [services_required_default, services_required_extra]
    )

    service_facts = host.ansible("service_facts")["ansible_facts"]["services"]

    for service_name in services_required:
        if not service_name + ".service" in service_facts:
            continue

        service = host.service(service_name)
        assert service.is_running
        assert service.is_enabled
