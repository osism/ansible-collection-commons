import pytest

from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "RedHat":
        pytest.skip("ansible_os_family mismatch")


def test_timezone_settings(host):
    check_ansible_os_family(host)

    timezone_name = get_variable(host, "timezone_name")
    timezone_hwclock = get_variable(host, "timezone_hwclock")

    timezone_file = host.file("/etc/localtime")
    assert timezone_file.exists
    assert timezone_file.is_symlink
    assert timezone_file.linked_to == f"/usr/share/zoneinfo/{timezone_name}"

    hwclock_file = host.file("/etc/adjtime")
    if hwclock_file.exists:
        assert timezone_hwclock in hwclock_file.content_string
