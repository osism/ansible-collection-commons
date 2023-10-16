import os
import pytest
from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_var(host):
    assert get_variable(host, "docker_compose_install_type") == "package"


def test_systemd(host):
    f = host.file("/etc/systemd/system/docker-compose@.service")
    assert f.exists
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o644


def test_apt_preference(host):
    f = host.file("/etc/apt/preferences.d/docker-compose")
    assert not f.exists


def test_pkg(host):
    # We do NOT want the compose package
    package_name = get_variable(host, "docker_compose_package_name")
    assert package_name != ""

    package = host.package(package_name)
    assert not package.is_installed

    # We want to have the plugin package
    package_name = get_variable(host, "docker_compose_plugin_package_name")
    assert package_name != ""

    package = host.package(package_name)
    assert package.is_installed


def test_wrapper_file(host):
    f = host.file("/usr/local/bin/docker-compose")
    assert f.exists
    assert f.is_file
    assert f.mode == 0o755
    assert f.content_string.strip() == """#!/usr/bin/env bash

# The docker-compose CLI has been removed in OSISM.
# The Compose plugin for Docker is now used.
# The plugin can be called via 'docker compose'.

/usr/bin/docker compose "$@"
""".strip()