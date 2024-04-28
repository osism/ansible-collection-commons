import pytest

from .util.util import get_ansible, get_variable, get_from_url, get_family_role_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_group(host):
    group = host.group(get_variable(host, "operator_group"))

    assert group.exists
    assert group.gid == get_variable(host, "operator_group_id")


def test_user(host):
    user = host.user(get_variable(host, "operator_user"))

    assert user.exists
    assert user.shell == get_variable(host, "operator_shell")
    assert user.uid == get_variable(host, "operator_user_id")
    assert user.group == get_variable(host, "operator_group")

    additional_groups = get_family_role_variable(host, "__operator_groups")
    for additional_group in additional_groups:
        assert additional_group in user.groups


def test_sudoersfile(host):
    user = get_variable(host, "operator_user")

    with host.sudo("root"):
        sudoers_file = host.file(f"/etc/sudoers.d/{user}-sudoers")

        assert sudoers_file.exists
        assert sudoers_file.user == "root"
        assert sudoers_file.group == "root"
        assert sudoers_file.mode == 0o440


def test_bashrc(host):
    user = host.user(get_variable(host, "operator_user"))
    assert user.exists

    bashrc_file = host.ansible("file", f"path={user.home}/.bashrc", become=True)
    assert bashrc_file["state"] == "file"
    assert bashrc_file["mode"] == "0640"

    with host.sudo(get_variable(host, "operator_user")):
        bashrc_content = host.check_output(f"cat {user.home}/.bashrc")

        lines = [
            "export LANGUAGE=C.UTF-8",
            "export LANG=C.UTF-8",
            "export LC_ALL=C.UTF-8",
        ]

        for line in lines:
            assert line in bashrc_content


def test_ssh(host):
    user = host.user(get_variable(host, "operator_user"))
    assert user.exists

    ssh_folder = host.ansible("file", f"path={user.home}/.ssh", become=True)
    assert ssh_folder["state"] == "directory"
    assert ssh_folder["mode"] == "0700"
    assert ssh_folder["owner"] == get_variable(host, "operator_user")
    assert ssh_folder["group"] == get_variable(host, "operator_group")


def test_sshkeys(host):
    user = host.user(get_variable(host, "operator_user"))
    assert user.exists

    expected_authorized_keys = get_variable(host, "operator_authorized_keys")

    if len(expected_authorized_keys) <= 0:
        pytest.skip("No operator_authorized_keys defined")

    authorized_keys_file = host.ansible(
        "file", f"path={user.home}/.ssh/authorized_keys", become=True
    )
    assert authorized_keys_file["state"] == "file"

    with host.sudo(get_variable(host, "operator_user")):
        authorized_keys_content = host.check_output(
            f"cat {user.home}/.ssh/authorized_keys"
        )

        for authorized_key in expected_authorized_keys:
            assert authorized_key in authorized_keys_content


def test_githubkeys(host):
    user = host.user(get_variable(host, "operator_user"))
    assert user.exists

    expected_github_accounts = get_variable(host, "operator_authorized_github_accounts")

    if len(expected_github_accounts) <= 0:
        pytest.skip("No operator_authorized_github_accounts defined")

    authorized_keys_file = host.ansible(
        "file", f"path={user.home}/.ssh/authorized_keys", become=True
    )
    assert authorized_keys_file["state"] == "file"

    with host.sudo(get_variable(host, "operator_user")):
        authorized_keys_content = host.check_output(
            f"cat {user.home}/.ssh/authorized_keys"
        )

        for github_user in expected_github_accounts:
            contents = get_from_url(f"https://github.com/{github_user}.keys").split(
                "\n"
            )

            for line in contents:
                line = line.strip()
                components = line.split(" ")

                if len(components) < 2:
                    continue

                assert components[0] in authorized_keys_content
                assert components[1] in authorized_keys_content


def test_password(host):
    password = None
    try:
        password = get_variable(host, "operator_password")
    except Exception:
        pytest.skip("No operator_password defined")

    if password is None or password == "":
        pytest.skip("operator_password is empty")

    with host.sudo("root"):
        user = host.user(get_variable(host, "operator_user"))
        assert user.password == password
