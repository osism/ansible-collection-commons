import pytest

from ..util.util import (
    get_ansible,
    get_variable,
    get_os_role_variable,
    jinja_list_concat,
)

testinfra_runner, testinfra_hosts = get_ansible()


def test_cleanup_pkg(host):
    packages = get_variable(host, "cleanup_packages")
    packages_default = get_variable(host, "cleanup_packages_default")
    packages_extra = get_variable(host, "cleanup_packages_extra")

    packages_distribution = get_os_role_variable(host, "cleanup_packages_distribution")

    packages = jinja_list_concat(
        packages, [packages_default, packages_extra, packages_distribution]
    )

    for package_name in packages:
        package = host.package(package_name)
        assert not package.is_installed


def test_cleanup_cloudimage(host):
    if not get_variable(host, "cleanup_cloudinit"):
        pytest.skip("cleanup_cloudinit is not True")

    package_name = get_os_role_variable(host, "cleanup_cloudinit_package_name")

    package = host.package(package_name)
    assert not package.is_installed
