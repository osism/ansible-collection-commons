from .util.util import get_variable


def test_runc_package_installed(host):
    """Check if the runc package is installed."""
    runc_package_name = get_variable(host, "runc_package_name")
    package = host.package(runc_package_name)
    assert package.is_installed


def test_runc_command_exists(host):
    """Check if the runc command is available."""
    assert host.exists("runc")
