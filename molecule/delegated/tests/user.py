import pytest

from .util.util import get_ansible, get_variable, get_from_url

testinfra_runner, testinfra_hosts = get_ansible()


def test_user_accounts_present(host):
    user_list = get_variable(host, "user_list")
    assert type(user_list) is list

    if len(user_list) == 0:
        pytest.skip("user_list is empty")

    for user_entry in user_list:
        user_name = user_entry["name"]

        assert host.group(user_name).exists

        user = host.user(user_name)
        assert user.exists
        assert user.shell == "/usr/bin/bash"
        assert user.group == user_name

        hd = host.file(f"/home/{user_name}")
        assert hd.exists
        assert hd.is_directory

        with host.sudo(user_name):
            keyfile = host.file(f"/home/{user_name}/.ssh/authorized_keys")
            assert keyfile.exists
            assert not keyfile.is_directory

            key = user_entry["key"]
            keyfile_content = keyfile.content_string

            if key.startswith("https") or key == "github":
                # Remote keys are fetched (delegated to the controller by
                # default via user_fetch_keys_delegate_to) and installed on
                # the target host. Verify each fetched key's type and
                # material landed in the keyfile.
                url = (
                    key
                    if key.startswith("https")
                    else f"https://github.com/{user_name}.keys"
                )

                # Collect the key lines actually served. Guard that the list
                # is non-empty so an empty response (e.g. the account removed
                # all its keys) fails loudly instead of skipping every
                # assertion below and passing while verifying nothing.
                key_lines = [
                    line.strip().split(" ")
                    for line in get_from_url(url).split("\n")
                    if len(line.strip().split(" ")) >= 2
                ]
                assert (
                    key_lines
                ), f"no keys fetched from {url}; cannot verify {user_name}"

                for components in key_lines:
                    assert components[0] in keyfile_content
                    assert components[1] in keyfile_content
            else:
                assert key in keyfile_content


def test_user_sudo(host):
    assert host.package("sudo").is_installed

    user_list = get_variable(host, "user_list")
    assert type(user_list) is list

    if len(user_list) == 0:
        pytest.skip("user_list is empty")

    for user_entry in user_list:
        user_name = user_entry["name"]

        with host.sudo("root"):
            f = host.file(f"/etc/sudoers.d/{user_name}")
            assert f.exists
            assert not f.is_directory
            assert f.mode == 0o440
            assert f.user == "root"
            assert f.group == "root"
            assert "NOPASSWD: ALL" in f.content_string


def test_user_accounts_absent(host):
    user_list = get_variable(host, "user_delete")
    assert type(user_list) is list

    if len(user_list) == 0:
        pytest.skip("user_delete is empty")

    for user_name in user_list:
        assert not host.group(user_name).exists

        user = host.user(user_name)
        assert not user.exists

        hd = host.file(f"/home/{user_name}")
        assert not hd.exists
