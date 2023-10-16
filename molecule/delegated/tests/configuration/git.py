import os
import pytest
import subprocess

from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def check_configuration_type(host):
    if get_variable(host, "configuration_type") != "git":
        pytest.skip("configuration_type mismatch")


def test_pkg(host):
    check_configuration_type(host)

    package_name = get_variable(host, "configuration_git_package_name")
    assert package_name != ""

    package = host.package(package_name)
    assert package.is_installed


def test_sshkey(host):
    check_configuration_type(host)

    protocol = get_variable(host, "configuration_git_protocol")
    private_key = get_variable(host, "configuration_git_private_key")
    
    if protocol != "ssh" or private_key is None or len(private_key) == 0:
        return

    private_key = "<hidden>"

    path = get_variable(host, "configuration_git_private_key_file")

    f = host.file(f"{path}")
    assert f.exists
    assert f.is_file
    assert f.user == get_variable(host, 'operator_user')
    assert f.group == get_variable(host, 'operator_group')
    assert f.mode == 0o600


def test_repo(host):
    check_configuration_type(host)

    path = get_variable(host, "configuration_directory")

    f = host.file(f"{path}")
    assert f.exists
    assert f.is_directory


def test_proxy(host):
    check_configuration_type(host)

    expected = get_variable(host, "configuration_git_proxy")

    if expected is None or len(expected) == 0:
        return

    actual = subprocess.run(["git", "config", "--global", "http.proxy"], capture_output=True, text=True).stdout

    assert expected == actual
