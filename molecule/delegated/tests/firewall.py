from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_firewall_config_file(host):
    f = host.file("/etc/ufw/ufw.conf")

    assert f.exists
    assert f.mode == 0o644


def test_firewall_service(host):
    service_name = get_variable(host, "ufw_service_name")
    service = host.service(service_name)

    assert service.is_running
    assert service.is_enabled
