import pytest

from ..util.util import (
    get_ansible,
    get_variable,
    get_from_url,
    extract_url_from_variable,
    get_centos_repo_key,
)

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "RedHat":
        pytest.skip("ansible_os_family mismatch")


def check_configure_repository(host):
    if not get_variable(host, "kubectl_configure_repository"):
        pytest.skip("kubectl_configure_repository is not set")


def test_kubectl_gpg_key_present(host):
    """Check if the GPG key for the kubectl repository is correctly added."""
    check_ansible_os_family(host)
    check_configure_repository(host)

    all_keys = host.run(
        "rpm -qa gpg-pubkey* --qf '%{NAME}-%{VERSION}-%{RELEASE} --> %{SUMMARY}\n%{DESCRIPTION}\n\n'"
    ).stdout
    installed_key = get_centos_repo_key(
        host,
        "isv:kubernetes OBS Project <isv:kubernetes@build.opensuse.org> public key",
    )
    assert installed_key in all_keys

    k8s_repository_key_url = get_variable(host, "kubectl_redhat_repository_key")
    key_content = get_from_url(k8s_repository_key_url)
    assert installed_key in key_content


def test_kubectl_repository_configured(host):
    """Check if the kubectl repository is correctly configured."""
    check_ansible_os_family(host)
    check_configure_repository(host)

    extracted_url = extract_url_from_variable(host, "kubectl_redhat_repository")

    with host.sudo("root"):
        repo_file = host.file("/etc/yum.repos.d/kubernetes.repo")

        assert repo_file.exists
        assert repo_file.user == "root"
        assert repo_file.group == "root"
        assert repo_file.mode == 0o644

    with host.sudo("root"):
        repo_file_content = host.check_output("cat /etc/yum.repos.d/kubernetes.repo")

    assert (
        extracted_url in repo_file_content
    ), "The extracted URL is not present in the kubectl configuration file"
