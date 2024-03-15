from ..util.util import (
    get_ansible,
    get_variable,
)

testinfra_runner, testinfra_hosts = get_ansible()


def test_kubectl_package_installed(host):
    """Check if the kubectl package is installed."""
    kubectl_package_name = get_variable(host, "kubectl_package_name")
    kubectl_pkg = host.package(kubectl_package_name)
    assert kubectl_pkg.is_installed
