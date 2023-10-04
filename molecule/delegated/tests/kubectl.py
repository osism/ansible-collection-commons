import pytest

from .util.util import (get_ansible, get_variable, get_from_url,
                        jinja_replacement)

testinfra_runner, testinfra_hosts = get_ansible()


def test_apt_transport_https_installed(host):
    """Check if the apt-transport-https package is installed."""
    kubectl_configure_repository = get_variable(
        host, "kubectl_configure_repository")

    if not kubectl_configure_repository:
        pytest.skip("kubectl_configure_repository is not set")

    pkg = host.package("apt-transport-https")
    assert pkg.is_installed


def test_kubectl_gpg_key_present(host):
    """Check if the GPG key for the kubectl repository is correctly added."""
    kubectl_configure_repository = get_variable(
        host, "kubectl_configure_repository")

    if not kubectl_configure_repository:
        pytest.skip("kubectl_configure_repository is not set")

    gpg_key_file = host.file("/usr/share/keyrings/kubectl.gpg")

    # Ensure the GPG key file exists
    assert gpg_key_file.exists

    # Ensure the correct permissions are set
    assert gpg_key_file.user == "root"
    assert gpg_key_file.group == "root"
    assert gpg_key_file.mode == 0o644

    kubectl_repository_key = get_variable(
        host, "kubectl_debian_repository_key")
    expected_key = get_from_url(kubectl_repository_key, True)

    assert gpg_key_file.content == expected_key


def test_kubectl_repository_configured(host):
    """Check if the kubectl repository is correctly configured."""
    kubectl_configure_repository = get_variable(
        host, "kubectl_configure_repository")

    if not kubectl_configure_repository:
        pytest.skip("kubectl_configure_repository is not set")

    kubectl_repository = get_variable(host, "kubectl_debian_repository")
    kubectl_debian_repository_arch = get_variable(
        host, "kubectl_debian_repository_arch")

    repo_file = host.file("/etc/apt/sources.list.d/kubectl.list")

    # Ensure the repository file exists
    assert repo_file.exists

    # Ensure the content matches the expected repository configuration
    formatted_kubectl_repository = jinja_replacement(
        kubectl_repository,
        {"kubectl_debian_repository_arch": kubectl_debian_repository_arch})

    assert formatted_kubectl_repository in repo_file.content_string


def test_kubectl_package_installed(host):
    """Check if the kubectl package is installed."""
    kubectl_package_name = get_variable(host, "kubectl_package_name")
    kubectl_pkg = host.package(kubectl_package_name)
    assert kubectl_pkg.is_installed
