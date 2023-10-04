import pytest

from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "Debian":
        pytest.skip("ansible_os_family mismatch")


def test_pkg(host):
    check_ansible_os_family(host)

    assert not host.package("update-motd").is_installed


def test_service(host):
    check_ansible_os_family(host)

    service_facts = host.ansible("service_facts")["ansible_facts"]["services"]

    if "motd-news.timer" in service_facts:
        assert not host.service("motd-news.timer").is_running
        # assert not host.service("motd-news.timer").is_enabled

    if "motd-news.service" in service_facts:
        assert not host.service("motd-news.service").is_running
        # assert not host.service("motd-news.service").is_enabled
