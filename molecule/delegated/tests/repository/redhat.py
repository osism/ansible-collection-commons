import pytest

from ..util.util import (
    get_ansible,
    get_variable,
    get_from_url,
    get_os_role_variable,
    jinja_replacement,
)

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "RedHat":
        pytest.skip("ansible_os_family mismatch")
