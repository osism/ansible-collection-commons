import pytest

from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def check_hosts_type(host):
    if get_variable(host, "hosts_type") != "block":
        pytest.skip("hosts_type mismatch")


def check_single_host(host, content):
    if get_variable(host, "hosts_use_dns_as_single_source_of_truth"):
        pytest.skip("hosts_use_dns_as_single_source_of_truth is True")

    host_name = get_variable(host, "inventory_hostname")
    if host_name in get_variable(host, "hosts_ignore"):
        pytest.skip(f"{host_name} is in hosts_ignore")

    hosts_enable = False
    try:
        hosts_enable = get_variable(host, "hosts_enable")
    except Exception:
        pytest.skip("hosts_enable is not defined")

    if not hosts_enable:
        pytest.skip("hosts_enable is not True")

    hosts_interface = None
    try:
        hosts_interface = get_variable(host, "hosts_interface")
    except Exception:
        pytest.skip("hosts_interface is not defined")

    ansible_interface = None
    try:
        ansible_interface = get_variable(host, "ansible_" + hosts_interface, True)
    except Exception:
        pytest.skip(f"ansible_{hosts_interface} is not defined")

    test_string = (
        f"{ansible_interface['ipv4']['address']} {host_name} {host_name.split('.')[0]}"
    )
    assert test_string in content


def test_hostfile(host):
    check_hosts_type(host)

    path = get_variable(host, "hosts_file")
    f = host.file(f"{path}")
    assert f.exists
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o644

    content = f.content_string

    assert "osism.hosts" in content

    check_single_host(host, content)

    additional_entries = get_variable(host, "hosts_additional_entries")
    for key, value in additional_entries.items():
        test_string = f"{value} {key} {key.split('.')[0]}"
        assert test_string in content
