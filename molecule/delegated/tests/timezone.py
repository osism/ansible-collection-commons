from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_tzdata_package(host):
    package = host.package('tzdata')
    assert package.is_installed


def test_timezone_settings(host):
    timezone_name = get_variable(host, 'timezone_name')
    timezone_hwclock = get_variable(host, 'timezone_hwclock')

    timezone_file = host.file('/etc/timezone')
    assert timezone_file.exists
    assert timezone_file.content_string.strip() == timezone_name

    hwclock_file = host.file('/etc/adjtime')
    if hwclock_file.exists:
        assert timezone_hwclock in hwclock_file.content_string
