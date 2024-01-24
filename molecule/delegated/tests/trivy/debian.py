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


def test_package(host):
    """Check if the packages are installed."""
    check_ansible_os_family(host)

    if get_variable(host, "trivy_configure_repository"):
        pkg_name = "apt-transport-https"
        pkg = host.package(pkg_name)
        assert pkg.is_installed

    pkg_name = get_variable(host, "trivy_package_name")
    pkg = host.package(pkg_name)
    assert pkg.is_installed


def test_trivy_gpg_key_present(host):
    """Check if the GPG key for the trivy repository is correctly added."""
    check_ansible_os_family(host)

    trivy_configure_repository = get_variable(host, "trivy_configure_repository")

    if not trivy_configure_repository:
        pytest.skip("trivy_configure_repository not configured")

    trivy_repository_key_url = get_variable(host, "trivy_debian_repository_key")

    # Fetch the GPG key content from the URL
    key_content = get_from_url(trivy_repository_key_url)

    # Validate the permissions and ownership of the GPG key file
    key_file = host.file("/etc/apt/trusted.gpg.d/trivy.asc")
    assert key_file.exists
    assert key_file.user == "root"
    assert key_file.group == "root"
    assert key_file.mode == 0o644
    assert key_file.content_string == key_content


def test_trivy_repository_configured(host):
    """Check if the Trivy repository is correctly configured."""
    check_ansible_os_family(host)

    trivy_configure_repository = get_variable(host, "trivy_configure_repository")

    if not trivy_configure_repository:
        pytest.skip("trivy_configure_repository not configured")

    extracted_url = extract_url_from_variable(host, "trivy_debian_repository")

    repo_file = host.file("/etc/apt/sources.list.d/trivy.list")
    assert repo_file.exists
    assert repo_file.user == "root"
    assert repo_file.group == "root"
    assert repo_file.mode == 0o600

    with host.sudo("root"):
        repo_file_content = host.check_output("cat /etc/apt/sources.list.d/trivy.list")
        assert (
            extracted_url in repo_file_content
        ), "The extracted URL is not present in the configuration file"
