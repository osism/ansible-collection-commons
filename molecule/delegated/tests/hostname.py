from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_hostname(host):
    # Fetch system's hostname using the 'hostname' command
    system_hostname = host.check_output("hostname")

    expected_hostname = None
    if get_variable(host, "hostname_use_fqdn"):
        expected_hostname = get_variable(host, "inventory_hostname")
    else:
        expected_hostname = get_variable(host, "inventory_hostname").split(".")[0]

    assert system_hostname == expected_hostname


def test_hostname_settings(host):
    etc_hostname = host.file("/etc/hostname")
    assert etc_hostname.exists
    assert etc_hostname.user == "root"
    assert etc_hostname.group == "root"
    assert etc_hostname.mode == 0o644

    expected_hostname = None
    if get_variable(host, "hostname_use_fqdn"):
        expected_hostname = get_variable(host, "inventory_hostname")
    else:
        expected_hostname = get_variable(host, "inventory_hostname").split(".")[0]

    assert etc_hostname.content_string.strip() == expected_hostname
