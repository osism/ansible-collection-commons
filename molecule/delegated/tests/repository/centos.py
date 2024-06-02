import pytest

from ..util.util import (
    get_ansible,
    get_variable,
    get_dist_role_variable,
    jinja_replacement,
)

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_distribution(host):
    if get_variable(host, "ansible_distribution", True) != "CentOS":
        pytest.skip("ansible_distribution mismatch")


def test_repository_centos_keys(host):
    check_ansible_distribution(host)

    key_file = host.file("/etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial")
    assert key_file.exists
    assert not key_file.is_directory


def test_repository_centos_files(host):
    check_ansible_distribution(host)

    repositories = get_variable(host, "repositories")

    if len(repositories) <= 0:
        repositories = get_dist_role_variable(host, "__repository_default")

    assert len(repositories) > 0

    ansible_distribution = get_variable(host, "ansible_distribution", True)

    for repository in repositories:
        repository["file"] = jinja_replacement(
            repository["file"],
            {"ansible_distribution": ansible_distribution},
        )

        with host.sudo("root"):
            f = host.file(f"/etc/yum.repos.d/{repository['file']}.repo")
            assert f.exists
            assert not f.is_directory
            assert repository["name"] in f.content_string
