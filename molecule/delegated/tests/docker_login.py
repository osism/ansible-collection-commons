from .util.util import get_ansible

testinfra_runner, testinfra_hosts = get_ansible()


def test_packages_installed(host):
    """Check if the gnupg2 and pass packages are installed."""

    # Check if gnupg2 is installed
    gnupg2_pkg = host.package("gnupg2")
    assert gnupg2_pkg.is_installed, "The gnupg2 package is not installed."

    # Check if pass is installed
    pass_pkg = host.package("pass")
    assert pass_pkg.is_installed, "The pass package is not installed."


# The actual login is done by the role itself so we don't explicitly test this here again.
