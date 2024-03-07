import pytest

from ..util.util import (
    get_ansible,
    get_variable,
    get_os_role_variable,
)

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "RedHat":
        pytest.skip("ansible_os_family mismatch")


# def test_keys(host):
#     check_ansible_os_family(host)
#
#     f = host.file("/etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial")
#     # to-do: test all keys
#     assert f.exists


def test_sources(host):
    check_ansible_os_family(host)

    f = host.file("/etc/yum.repos.d/centos.repo")
    assert f.exists
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o644

    repositories = get_variable(host, "repositories")

    if len(repositories) <= 0:
        repositories = get_os_role_variable(host, "repository_default", "CentOS.yml")

    assert len(repositories) > 0

    print(repositories)

    # for repository in repositories:
    # ansible_distribution = get_variable(host, "ansible_distribution", True)
    # repository["file"] = jinja_replacement(
    #     repository["file"],
    #     {"ansible_distribution": ansible_distribution},
    # )
    # #assert repository["file"] in f.content_string

    # assert repository["name"] in f.content_string
    #
    # if "mirrorlist" in repository:
    #     # assert repository["mirrorlist"].split("=epel")[0] in f.content_string
    #     assert "http://mirrorlist.centos.org" in f.content_string
    #
    # if "metalink" in repository:
    #     # assert (repository["metalink"]).split("=epel")[0] in f.content_string
    #     assert "https://mirrors.fedoraproject.org" in f.content_string

    # key = (repository["gpgkey"]).split("://")[1]
    # key_file = host.file(key)

    # testing only: repository_default in CentOS.yml obsolet?
    key_file = host.file("/etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial")
    assert key_file.exists
