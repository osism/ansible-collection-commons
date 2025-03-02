import pytest
import socket

from .util.util import (
    get_ansible,
    get_variable,
    jinja_list_concat,
)

testinfra_runner, testinfra_hosts = get_ansible()


def get_expected_nameservers(host):
    """Get the list of expected nameservers by resolving Jinja2 templates and combining lists."""

    expected_nameservers = get_variable(host, "resolvconf_nameserver")
    expected_nameservers_default = get_variable(host, "resolvconf_nameserver_default")
    expected_nameservers_extra = get_variable(host, "resolvconf_nameserver_extra")

    return jinja_list_concat(
        expected_nameservers, [expected_nameservers_default, expected_nameservers_extra]
    )


def test_resolvconf_minimum_number_of_nameservers(host):
    """Check the minimum number of nameservers."""

    nameservers = get_variable(host, "resolvconf_nameserver")
    minimum_ns = get_variable(host, "resolvconf_minimum_number_of_nameservers")
    assert len(nameservers) >= minimum_ns


def test_resolvconf_service_disabled(host):
    """Check if the resolvconf service is disabled."""

    service = host.service("resolvconf")
    cmd = host.run(
        f'systemctl list-units --all | grep -q "^[[:space:]]*{service.name}"'
    )
    if cmd.rc == 0:
        assert not service.is_enabled
        assert not service.is_running
    else:
        pytest.skip("The resolvconf service does not exist")


def test_resolved_conf_file(host):
    """Check if the resolved.conf file exists and its permissions."""

    resolved_file = host.file("/etc/systemd/resolved.conf")
    assert resolved_file.exists
    assert resolved_file.user == "root"
    assert resolved_file.group == "root"
    assert resolved_file.mode == 0o644
    assert "DO NOT EDIT THIS FILE BY HAND" in resolved_file.content_string


def test_resolvconf_content(host):
    """Check content of /etc/systemd/resolved.conf."""

    file_content = host.file("/etc/systemd/resolved.conf").content_string

    assert f"Domains={get_variable(host, 'resolvconf_search')}" in file_content

    dnssec = get_variable(host, "resolvconf_dnssec")
    if type(dnssec) is str:
        assert f"DNSSEC={dnssec}" in file_content
    else:
        assert f"DNSSEC={'yes' if dnssec is True else 'no'}" in file_content

    fallback_dns_servers = get_variable(host, "resolvconf_fallback_nameserver")
    if len(fallback_dns_servers) > 0:
        for fallback_dns_server in fallback_dns_servers:
            assert fallback_dns_server in file_content

    dnstls = get_variable(host, "resolvconf_dns_over_tls")
    if type(dnstls) is str:
        assert f"DNSOverTLS={dnstls}" in file_content
    else:
        assert f"DNSOverTLS={'yes' if dnstls is True else 'no'}" in file_content

    resolvecache = get_variable(host, "resolvconf_cache")
    if type(resolvecache) is str:
        assert f"Cache={resolvecache}" in file_content
    else:
        assert f"Cache={'yes' if resolvecache is True else 'no'}" in file_content

    cachelocal = get_variable(host, "resolvconf_cache_from_localhost")
    assert f"CacheFromLocalhost={'yes' if cachelocal is True else 'no'}" in file_content

    etchosts = get_variable(host, "resolvconf_read_etc_hosts")
    assert f"ReadEtcHosts={'yes' if etchosts is True else 'no'}" in file_content

    expected_nameservers = get_expected_nameservers(host)
    assert type(expected_nameservers) is list

    for expected in expected_nameservers:
        assert expected in file_content


def test_systemd_resolved_service_enabled(host):
    """Check if the systemd-resolved service is enabled and running."""

    service = host.service("systemd-resolved")
    assert service.is_enabled
    assert service.is_running


def test_resolvconf_file_is_symlink(host):
    """Check if /etc/resolv.conf is a symlink."""

    resolvconf_file = get_variable(host, "resolvconf_file")
    f = host.file(resolvconf_file)
    assert f.is_symlink


def test_dns_resolution(host):
    """Check if DNS resolution is working correctly."""

    expected_nameservers = get_expected_nameservers(host)

    for nameserver in expected_nameservers:
        cmd = host.run(f"dig @{nameserver} osism.tech +short")
        assert cmd.rc == 0
        assert cmd.stdout.strip() != ""


def test_dns_reverse_lookup(host):
    """Check if reverse DNS lookup is working."""

    expected_nameservers = get_expected_nameservers(host)

    for nameserver in expected_nameservers:
        ip = socket.gethostbyname("osism.tech")
        cmd = host.run(f"dig @{nameserver} -x {ip} +short")
        assert cmd.rc == 0
        assert cmd.stdout.strip() != ""
