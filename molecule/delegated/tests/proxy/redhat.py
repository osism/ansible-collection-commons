import pytest

from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "RedHat":
        pytest.skip("ansible_os_family mismatch")


def test_yum_proxy_configuration(host):
    """Check if the proxy configuration for yum is correctly set on RedHat-based systems."""
    check_ansible_os_family(host)

    proxy_proxies = get_variable(host, "proxy_proxies")
    proxy_package_manager = get_variable(host, "proxy_package_manager")

    if len(proxy_proxies) == 0:
        pytest.skip("proxy_proxies is empty")

    if not proxy_package_manager:
        pytest.skip("proxy_package_manager is not true")

    fastestmirror_file = host.file("/etc/yum/pluginconf.d/fastestmirror.conf")

    # Check if the fastestmirror plugin is disabled
    assert fastestmirror_file.exists
    assert fastestmirror_file.mode == 0o644
    assert "enabled=0" in fastestmirror_file.content_string

    yum_conf_file = host.file("/etc/yum.conf")
    assert yum_conf_file.exists
    assert yum_conf_file.mode == 0o644

    # Check if the proxy configuration in the yum conf matches the expected values
    if 'http' in proxy_proxies:
        assert f"proxy={proxy_proxies['http']}" in yum_conf_file.content_string
    if 'https' in proxy_proxies:
        assert f"proxy={proxy_proxies['https']}" in yum_conf_file.content_string
