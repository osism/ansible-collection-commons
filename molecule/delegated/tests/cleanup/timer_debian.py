import pytest

from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "Debian":
        pytest.skip("ansible_os_family mismatch")


def test_cleanup_timer(host):
    check_ansible_os_family(host)

    service_facts = host.ansible("service_facts")["ansible_facts"]["services"]

    for service_name in ["apt-daily-upgrade.timer", "apt-daily.timer"]:
        if service_name + ".timer" not in service_facts:
            continue

        service = host.service(service_name)
        assert not service.is_enabled
        assert not service.is_running
