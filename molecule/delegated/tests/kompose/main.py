from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_kompose_not_installed(host):
    package_name = "kompose"
    package = host.package(package_name)
    assert not package.is_installed


def test_kompose_binary_exists(host):
    kompose_path = "/usr/local/bin/kompose"
    f = host.file(kompose_path)
    assert f.exists
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o755


def test_kompose_binary_checksum(host):
    ansible_arch = get_variable(host, "ansible_architecture", True)
    kompose_checksums = get_variable(host, "kompose_checksums")
    kompose_path = "/usr/local/bin/kompose"

    if ansible_arch == "x86_64":
        kompose_checksum = kompose_checksums.get("amd64")
        f = host.file(kompose_path)
        assert f.exists
        assert f.sha256sum == kompose_checksum

    if ansible_arch == "aarch64" or ansible_arch == "arm64":
        kompose_checksum = kompose_checksums.get("arm64")
        f = host.file(kompose_path)
        assert f.exists
        assert f.sha256sum == kompose_checksum

    if ansible_arch == "armv6l" or ansible_arch == "armv7l":
        kompose_checksum = kompose_checksums.get("arm")
        f = host.file(kompose_path)
        assert f.exists
        assert f.sha256sum == kompose_checksum
