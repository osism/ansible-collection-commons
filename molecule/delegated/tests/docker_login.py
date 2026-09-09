import json

from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_packages_installed(host):
    """Check if the gnupg2 and pass packages are installed."""

    # Check if gnupg2 is installed
    gnupg2_pkg = host.package("gnupg2")
    assert gnupg2_pkg.is_installed, "The gnupg2 package is not installed."

    # Check if pass is installed
    pass_pkg = host.package("pass")
    assert pass_pkg.is_installed, "The pass package is not installed."


def _assert_login(host, user):
    """Check that the credentials of the registry are stored for a user."""

    registry = get_variable(host, "docker_login_registry")

    with host.sudo(user):
        home = host.user(user).home
        config = host.file(f"{home}/.docker/config.json")

        assert config.exists, f"No docker configuration file for the user {user}."
        assert registry in json.loads(config.content_string).get(
            "auths", {}
        ), f"No credentials for the registry {registry} for the user {user}."


def test_login_as_root(host):
    """Check that the login was done for the root user."""

    _assert_login(host, "root")


def test_login_as_operator(host):
    """Check that the login was done for the operator user."""

    _assert_login(host, get_variable(host, "docker_login_operator_user"))
