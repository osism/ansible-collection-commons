import pytest

from ..util.util import get_ansible, get_variable, get_from_url

testinfra_runner, testinfra_hosts = get_ansible()


def check_user_manage_type(host):
    if get_variable(host, "user_manage_type") != "keyfile":
        pytest.skip("user_manage_type mismatch")


def test_keyfile(host):
    check_user_manage_type(host)

    user_list = get_variable(host, "user_list")
    assert type(user_list) is list

    if len(user_list) == 0:
        pytest.skip("user_list is empty")

    f = host.file(get_variable(host, "user_manager_file"))
    assert f.exists
    assert not f.is_directory

    for user_entry in user_list:
        name = user_entry["name"]
        keys = get_from_url(user_entry["key"]).split("\n")
        for key in keys:
            assert f"{key} {name}" in f.content_string
