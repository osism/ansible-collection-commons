from .util.util import get_ansible

testinfra_runner, testinfra_hosts = get_ansible()


def test_srv(host):
    service = host.service("sys-kernel-config.mount")

    assert service.is_running
    assert service.is_enabled
