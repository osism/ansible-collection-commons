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

    service_user = get_variable(host, "docker_compose_service_user")
    assert f"User={service_user}" in f.content_string


def test_osism_target(host):
    f = host.file("/etc/systemd/system/osism.target")
    assert f.exists
    assert f.is_file
    assert f.mode == 0o644
    assert host.service("osism.target").is_enabled
    assert (
        "OSISM target allowing to start/stop all OSISM service at once"
        in f.content_string
    )


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

    if not f.exists:
        pytest.skip("Wrapper file does not exist.")

    assert f.exists
    assert f.is_file
    assert f.mode == 0o755
    assert (
        f.content_string.strip()
        == """#!/usr/bin/env bash

# The docker-compose CLI has been removed in OSISM.
# The Compose plugin for Docker is now used.
# The plugin can be called via 'docker compose'.

/usr/bin/docker compose "$@"
""".strip()
    )
