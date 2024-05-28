from ..util.util import (
    get_ansible,
    get_family_role_variable,
)

testinfra_runner, testinfra_hosts = get_ansible()


def test_packages(host):

    required_packages = get_family_role_variable(host, "kubectl_required_packages")
    assert type(required_packages) is list

    for package_name in required_packages:
        package = host.package(package_name)
        assert package.is_installed
