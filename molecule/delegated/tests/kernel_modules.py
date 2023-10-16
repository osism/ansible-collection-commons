import os
import pytest
from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


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
