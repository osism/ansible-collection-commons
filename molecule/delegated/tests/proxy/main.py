import pytest

from ..util.util import get_ansible, get_variable, jinja_list_concat

testinfra_runner, testinfra_hosts = get_ansible()


def test_proxy_settings(host):
    """Check if the system-wide proxy settings in /etc/environment are correctly set."""
    proxy_proxies = get_variable(host, "proxy_proxies")

    if len(proxy_proxies) == 0:
        pytest.skip("proxy_proxies is empty")

    env_file = host.file("/etc/environment")

    assert "ANSIBLE MANAGED BLOCK" in env_file.content_string

    if "http" in proxy_proxies:
        assert f"http_proxy={proxy_proxies['http']}" in env_file.content_string
    if "https" in proxy_proxies:
        assert f"https_proxy={proxy_proxies['https']}" in env_file.content_string
    if "ftp" in proxy_proxies:
        assert f"ftp_proxy={proxy_proxies['ftp']}" in env_file.content_string
    if "rsync" in proxy_proxies:
        assert f"rsync_proxy={proxy_proxies['rsync']}" in env_file.content_string

    proxy_no_proxy = get_variable(host, "proxy_no_proxy")
    proxy_no_proxy_default = get_variable(host, "proxy_no_proxy_default")
    proxy_no_proxy_extra = get_variable(host, "proxy_no_proxy_extra")

    proxy_no_proxy = jinja_list_concat(
        proxy_no_proxy, [proxy_no_proxy_default, proxy_no_proxy_extra]
    )

    no_proxy_string = f"no_proxy={','.join(proxy_no_proxy)}"
    assert no_proxy_string in env_file.content_string
