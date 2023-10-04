import pytest

from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def check_cleanup_cloudinit(host):
    if not get_variable(host, "cleanup_cloudinit"):
        pytest.skip("cleanup_cloudinit mismatch")


def test_file_absent(host):
    check_cleanup_cloudinit(host)

    f = host.file("/etc/cloud")
    assert not f.exists
