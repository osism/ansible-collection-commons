import os
import pytest
from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()

def test_microcode_packages(host):
    microcode_packages_default = get_variable(host, 'microcode_packages_default')
    microcode_packages_extra = get_variable(host, 'microcode_packages_extra')

    assert type(microcode_packages_default) is list
    assert type(microcode_packages_extra) is list

    microcode_packages = microcode_packages_default + microcode_packages_extra
    assert len(microcode_packages) > 0

    for package_name in microcode_packages:
        package = host.package(package_name)
        assert package.is_installed
