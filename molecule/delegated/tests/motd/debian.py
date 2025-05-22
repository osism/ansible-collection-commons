import pytest

from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "Debian":
        pytest.skip("ansible_os_family mismatch")


def test_pkg(host):
    check_ansible_os_family(host)
    assert not host.package("update-motd").is_installed


def test_motd_news_disabled(host):
    check_ansible_os_family(host)

    motd_news_file = host.file("/etc/default/motd-news")
    if motd_news_file.exists:
        assert "ENABLED=0" in motd_news_file.content_string


def test_pam_motd_removed(host):
    check_ansible_os_family(host)

    pam_files = host.run("grep -r 'pam_motd.so' /etc/pam.d/ || true")
    if pam_files.stdout:
        lines = pam_files.stdout.strip().split("\n")
        for line in lines:
            assert not (
                "session" in line and "optional" in line and "pam_motd.so" in line
            )
