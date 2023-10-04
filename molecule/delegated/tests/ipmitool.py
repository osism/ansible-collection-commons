import pytest

from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def is_virtual_machine(host):
    """Check if the host is running inside a virtual machine."""
    cmd = host.run("systemd-detect-virt --quiet")
    return cmd.rc == 0


def test_ipmitool_package_installed(host):
    """Check if the ipmitool package is installed."""
    package_name = get_variable(host, "ipmitool_package_name")
    package = host.package(package_name)
    assert package.is_installed


def test_kernel_modules_loaded(host):
    """Verify that the required kernel modules are loaded."""
    # Skip the test if running inside a virtual machine
    if is_virtual_machine(host):
        pytest.skip("Running inside virtual machine")

    # List of kernel modules to check
    kernel_modules = get_variable(host, "ipmitool_kernel_modules")
    assert type(kernel_modules) is list

    for module in kernel_modules:
        cmd = host.run(f"lsmod | grep {module}")
        assert cmd.rc == 0


def test_kernel_modules_persisted(host):
    """Check if the kernel modules are set to be loaded persistently."""
    # Skip the test if running inside a virtual machine
    if is_virtual_machine(host):
        pytest.skip("Running inside virtual machine")

    kernel_modules = get_variable(host, "ipmitool_kernel_modules")
    assert type(kernel_modules) is list

    for module in kernel_modules:
        # Verify each module's configuration exists in /etc/modules-load.d/
        module_file = host.file(f"/etc/modules-load.d/{module}.conf")
        assert module_file.exists
        assert module_file.contains(module)
        assert module_file.user == 'root'
        assert module_file.group == 'root'
        assert module_file.mode == 0o644
