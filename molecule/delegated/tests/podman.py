from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_pkg(host):
    package_name = get_variable(host, "podman_package_name")
    assert package_name != ""

    package = host.package(package_name)
    assert package.is_installed

    package_name = "uidmap"
    package = host.package(package_name)
    assert package.is_installed
