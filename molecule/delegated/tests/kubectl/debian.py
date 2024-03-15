import pytest

from ..util.util import (
    get_ansible,
    get_variable,
    extract_url_from_variable,
)

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "Debian":
        pytest.skip("ansible_os_family mismatch")


def check_configure_repository(host):
    if not get_variable(host, "kubectl_configure_repository"):
        pytest.skip("kubectl_configure_repository is not set")


def test_apt_transport_https_installed(host):
    """Check if the apt-transport-https package is installed."""
    check_ansible_os_family(host)
    check_configure_repository(host)

    pkg = host.package("apt-transport-https")
    assert pkg.is_installed


def test_kubectl_gpg_key_present(host):
    """Check if the GPG key for the kubectl repository is correctly added."""
    check_ansible_os_family(host)
    check_configure_repository(host)

    gpg_key_file = host.file("/etc/apt/keyrings/kubernetes-apt-keyring.gpg")
    assert gpg_key_file.exists
    assert gpg_key_file.user == "root"
    assert gpg_key_file.group == "root"
    assert gpg_key_file.mode == 0o644


def test_kubectl_repository_configured(host):
    """Check if the kubectl repository is correctly configured."""
    check_ansible_os_family(host)
    check_configure_repository(host)

    repo_file = host.file("/etc/apt/sources.list.d/kubectl.list")
    assert repo_file.exists
    assert repo_file.user == "root"
    assert repo_file.group == "root"

    with host.sudo("root"):
        repo_file_content = host.check_output(
            "cat /etc/apt/sources.list.d/kubectl.list"
        )
        extracted_url = extract_url_from_variable(host, "kubectl_debian_repository")
        assert (
            extracted_url in repo_file_content
        ), "The extracted URL is not present in the kubectl configuration file"


def test_kubectl_package_installed(host):
    """Check if the kubectl package is installed."""
    kubectl_package_name = get_variable(host, "kubectl_package_name")
    kubectl_pkg = host.package(kubectl_package_name)
    assert kubectl_pkg.is_installed
