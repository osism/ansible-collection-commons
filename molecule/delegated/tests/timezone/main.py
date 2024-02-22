from ..util.util import get_ansible

testinfra_runner, testinfra_hosts = get_ansible()


def test_tzdata_package(host):
    package = host.package("tzdata")
    assert package.is_installed
