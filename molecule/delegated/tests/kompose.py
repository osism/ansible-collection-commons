from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_kompose_not_installed(host):
    package_name = "kompose"
    package = host.package(package_name)
    assert not package.is_installed


def test_kompose_preferences_file(host):
    f = host.file("/etc/apt/preferences.d/kompose")
    assert f.exists
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o644
    assert "Pin-Priority: -1" in f.content_string


def test_kompose_binary_exists(host):
    kompose_path = "/usr/local/bin/kompose"
    f = host.file(kompose_path)
    assert f.exists
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o755


def test_kompose_binary_checksum(host):
    kompose_checksum = get_variable(host, "kompose_checksum")
    kompose_path = "/usr/local/bin/kompose"
    f = host.file(kompose_path)
    assert f.exists
    assert f.sha256sum == kompose_checksum
