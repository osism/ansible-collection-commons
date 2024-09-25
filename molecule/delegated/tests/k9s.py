from .util.util import get_ansible

testinfra_runner, testinfra_hosts = get_ansible()


def test_package(host):
    package = host.package("k9s")
    assert package.is_installed


def test_cli(host):
    result = host.run("k9s info")
    assert result.rc == 0
    assert "version" in result.stdout.lower()
