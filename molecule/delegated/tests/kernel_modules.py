import os
import pytest
import testinfra.utils.ansible_runner

testinfra_runner = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE'])
testinfra_hosts = testinfra_runner.get_hosts('all')


def get_variable(host, name):
    result = host.ansible('debug', f'var={name}')
    value = result.get(name, "VARIABLE IS NOT DEFINED!")

    if value.startswith('VARIABLE IS NOT DEFINED!'):
        default_vars = host.ansible("include_vars", "../../roles/kernel_modules/defaults/main.yml")["ansible_facts"]
        value = default_vars.get(name, "VARIABLE IS NOT DEFINED!")

    return value


def test_kernel_modules_in_etc_modules(host):
    kernel_modules_default = get_variable(host, 'kernel_modules_default')
    kernel_modules_extra = get_variable(host, 'kernel_modules_extra')
    kernel_modules = kernel_modules_default + kernel_modules_extra

    with host.sudo():
        etc_modules = host.file("/etc/modules").content_string.splitlines()

    for module in kernel_modules:
        assert module in etc_modules, f"Kernel module {module} not found in /etc/modules"


def test_loaded_kernel_modules(host):
    kernel_modules_default = get_variable(host, 'kernel_modules_default')
    kernel_modules_extra = get_variable(host, 'kernel_modules_extra')
    kernel_modules = kernel_modules_default + kernel_modules_extra

    with host.sudo():
        loaded_modules = host.check_output("lsmod").splitlines()

    for module in kernel_modules:
        assert any(module in line for line in loaded_modules), f"Kernel module {module} is not loaded"
