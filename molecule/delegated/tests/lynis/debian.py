import pytest

from ..util.util import (
    get_ansible,
    get_variable,
    get_from_url,
    extract_url_from_variable,
)

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "Debian":
        pytest.skip("ansible_os_family mismatch")


def test_apt_transport_https_installed(host):
    """Check if the apt-transport-https package is installed."""

    check_ansible_os_family(host)
    lynis_configure_repository = get_variable(host, "lynis_configure_repository")

    if not lynis_configure_repository:
        pytest.skip("lynis_configure_repository is not defined")

    pkg = host.package("apt-transport-https")
    assert pkg.is_installed


def test_lynis_gpg_key_present(host):
    """Check if the GPG key for the lynis repository is correctly added."""

    check_ansible_os_family(host)
    lynis_configure_repository = get_variable(host, "lynis_configure_repository")

    if not lynis_configure_repository:
        pytest.skip("lynis_configure_repository is not defined")

    lynis_repository_key_url = get_variable(host, "lynis_debian_repository_key")

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
    """Check if the Lynis repository is correctly configured."""

    check_ansible_os_family(host)
    lynis_configure_repository = get_variable(host, "lynis_configure_repository")

    if not lynis_configure_repository:
        pytest.skip("lynis_configure_repository is not defined")

    # Extract the URL from the configuration
    extracted_url = extract_url_from_variable(host, "lynis_debian_repository")

    # Validate the permissions and ownership of the repository file
    repo_file = host.file("/etc/apt/sources.list.d/lynis.list")
    assert repo_file.exists
    assert repo_file.user == "root"
    assert repo_file.group == "root"
    assert repo_file.mode == 0o600

    # Use sudo to read the content of the file
    with host.sudo("root"):
        repo_file_content = host.check_output("cat /etc/apt/sources.list.d/lynis.list")

    # Validate the content of the file
    assert (
        extracted_url in repo_file_content
    ), "The extracted URL is not present in the Lynis configuration file"


def test_lynis_package_installed(host):
    """Check if the lynis package is installed."""

    check_ansible_os_family(host)
    lynis_pkg_name = get_variable(host, "lynis_package_name")
    lynis_pkg = host.package(lynis_pkg_name)
    assert lynis_pkg.is_installed
