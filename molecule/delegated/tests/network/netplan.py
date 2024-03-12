import pytest
import os

from ..util.util import (
    get_ansible,
    get_variable,
    get_os_role_variable,
)

testinfra_runner, testinfra_hosts = get_ansible()


def check_network_type(host):
    if get_variable(host, "network_type") != "netplan":
        pytest.skip("network_type mismatch")


def test_packages(host):
    check_network_type(host)

    required_packages = get_os_role_variable(host, "network_netplan_required_packages")
    assert type(required_packages) is list

    for package_name in required_packages:
        package = host.package(package_name)
        assert package.is_installed

    removed_package = host.package("ifupdown")
    assert not removed_package.is_installed

    if get_variable(host, "ansible_os_family", True) == "Debian":
        network_dispatcher = get_os_role_variable(
            host, "network_dispatcher_package_name"
        )
        package = host.package(network_dispatcher)
        assert package.is_installed


def test_directory(host):
    check_network_type(host)

    directory = get_variable(host, "network_netplan_path")
    d = host.file(directory)

    assert d.exists
    assert d.is_directory
    assert d.mode == 0o755
    assert d.user == "root"
    assert d.group == "root"


def test_config_files(host):
    check_network_type(host)

    f = host.file(
        f"{get_variable(host, 'network_netplan_path')}/{get_variable(host, 'network_netplan_file')}"
    )

    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o600
    assert f.user == "root"
    assert f.group == "root"

    with host.sudo():
        assert "renderer: networkd" in f.content_string


def test_interfaces_file(host):
    check_network_type(host)

    f = host.file(f"{get_variable(host, 'network_interfaces_path')}")

    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o644
    assert f.user == "root"
    assert f.group == "root"


def test_service(host):
    check_network_type(host)

    service_name = get_os_role_variable(host, "network_dispatcher_service_name")
    service = host.service(service_name)

    assert service.is_running
    assert service.is_enabled


def test_cleanup(host):
    check_network_type(host)

    netplan_dir = get_variable(host, "network_netplan_path")
    netplan_path = host.file(netplan_dir)
    d = str(netplan_path.path)

    assert len(os.listdir(d)) == 1
