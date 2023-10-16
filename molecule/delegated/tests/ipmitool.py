from .util.util import get_ansible

testinfra_runner, testinfra_hosts = get_ansible()

def is_virtual_machine(host):
    """Check if the host is running inside a virtual machine."""
    cmd = host.run("systemd-detect-virt --quiet")
    return cmd.rc == 0

def test_ipmitool_package_installed(host):
    """Check if the ipmitool package is installed."""
    package = host.package("ipmitool")
    assert package.is_installed

def test_kernel_modules_loaded(host):
    """Verify that the required kernel modules are loaded."""
    # Skip the test if running inside a virtual machine
    if is_virtual_machine(host):
        return

    # List of kernel modules to check
    kernel_modules = ["ipmi_devintf", "ipmi_si"]

    for module in kernel_modules:
        cmd = host.run(f"lsmod | grep {module}")
        assert cmd.rc == 0, f"Module {module} not loaded. stdout: {cmd.stdout}, stderr: {cmd.stderr}"

def test_kernel_modules_persisted(host):
    """Check if the kernel modules are set to be loaded persistently."""
    # Skip the test if running inside a virtual machine
    if is_virtual_machine(host):
        return

    kernel_modules = ["ipmi_devintf", "ipmi_si"]

    for module in kernel_modules:
        # Verify each module's configuration exists in /etc/modules-load.d/
        module_file = host.file(f"/etc/modules-load.d/{module}.conf")
        assert module_file.exists, f"Configuration for module {module} not found"
        assert module_file.contains(module), f"Module {module} not in configuration file"
        assert module_file.user == 'root'
        assert module_file.group == 'root'
        assert oct(module_file.mode) == '0o644'
