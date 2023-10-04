import pytest

from .util.util import (get_ansible, get_variable, get_from_url,
                        jinja_replacement)

testinfra_runner, testinfra_hosts = get_ansible()


def test_apt_transport_https_installed(host):
    """Check if the apt-transport-https package is installed."""
    lynis_configure_repository = get_variable(
        host, "lynis_configure_repository")

    if not lynis_configure_repository:
        pytest.skip("lynis_configure_repository is not defined")

    pkg = host.package("apt-transport-https")
    assert pkg.is_installed


def test_lynis_gpg_key_present(host):
    """Check if the GPG key for the lynis repository is correctly added."""

    lynis_configure_repository = get_variable(
        host, "lynis_configure_repository")

    if not lynis_configure_repository:
        pytest.skip("lynis_configure_repository is not defined")

    lynis_repository_key_url = get_variable(
        host, "lynis_debian_repository_key")

    # Fetch the GPG key content from the URL
    key_content = get_from_url(f"{lynis_repository_key_url}")

    # Validate the permissions and ownership of the GPG key file
    key_file = host.file("/etc/apt/trusted.gpg.d/lynis.asc")
    assert key_file.exists
    assert key_file.user == "root"
    assert key_file.group == "root"
    assert key_file.mode == 0o644
    assert key_file.content_string == key_content


def test_lynis_repository_configured(host):
    """Check if the lynis repository is correctly configured."""

    lynis_configure_repository = get_variable(
        host, "lynis_configure_repository")

    if not lynis_configure_repository:
        pytest.skip("lynis_configure_repository is not defined")

    # Fetch the necessary variables from Ansible
    lynis_configure_repository = get_variable(
        host, "lynis_configure_repository")
    lynis_repository_arch = get_variable(host, "lynis_debian_repository_arch")
    lynis_repository = get_variable(host, "lynis_debian_repository")
    lynis_repository = jinja_replacement(
        lynis_repository,
        {"lynis_debian_repository_arch": lynis_repository_arch})

    # Validate the permissions and ownership of the repository file
    repo_file = host.file("/etc/apt/sources.list.d/lynis.list")
    assert repo_file.exists
    assert repo_file.user == "root"
    assert repo_file.group == "root"
    assert repo_file.mode == 0o600

    # Use sudo to read the content of the file
    with host.sudo("root"):
        repo_file_content = host.check_output(
            "cat /etc/apt/sources.list.d/lynis.list")

    # Validate the content of the file
    assert lynis_repository in repo_file_content


def test_lynis_package_installed(host):
    """Check if the lynis package is installed."""
    lynis_pkg_name = get_variable(host, "lynis_package_name")
    lynis_pkg = host.package(lynis_pkg_name)
    assert lynis_pkg.is_installed
