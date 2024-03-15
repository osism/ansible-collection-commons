import pytest

from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "RedHat":
        pytest.skip("ansible_os_family mismatch")


def test_kompose_preferences_file(host):
    check_ansible_os_family(host)

    f = host.file("/etc/yum.repos.d/kompose.repo")
    assert f.exists
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o644
    assert "name=block kompose package installation" in f.content_string
