import os
import pytest
from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()

def test_motd_content(host):
    motd_path = get_variable(host, 'motd_path')
    expected_motd_content = get_variable(host, 'motd_content')

    motd_file = host.file(motd_path)
    assert motd_file.exists
    assert motd_file.is_file
    assert motd_file.content_string.strip() == expected_motd_content.strip()

def test_issue_content(host):
    issue_path = get_variable(host, 'issue_path')
    expected_issue_content = get_variable(host, 'motd_content')

    issue_file = host.file(issue_path)
    assert issue_file.exists
    assert issue_file.is_file
    assert issue_file.content_string.strip() == expected_issue_content.strip()

def test_os_specific(host):
    ansible_os_family = host.system_info.distribution
    if ansible_os_family.lower() == "debian":
        assert not host.package("update-motd").is_installed
        assert not host.service("motd-news.timer").is_running
        assert not host.service("motd-news.service").is_running
        # Additional tests for Debian specific configurations
    elif ansible_os_family.lower() == "redhat":
        # RedHat specific tests (seems you have none for now)
        pass
