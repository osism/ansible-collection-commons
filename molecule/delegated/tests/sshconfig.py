from .util.util import get_ansible, get_variable, jinja_replacement

testinfra_runner, testinfra_hosts = get_ansible()


def test_sshconfig_directory(host):
    operator_user_name = get_variable(host, "operator_user")
    operator_user = host.user(operator_user_name)

    ssh_config_d = host.file(f"{operator_user.home}/.ssh/config.d")
    assert ssh_config_d.is_directory
    assert ssh_config_d.user == operator_user_name
    assert ssh_config_d.group == get_variable(host, "operator_group")
    assert ssh_config_d.mode == 0o700


def test_sshconfig_host_files(host):
    operator_user_name = get_variable(host, "operator_user")
    operator_user = host.user(operator_user_name)
    sshconfig_order = get_variable(host, "sshconfig_order")
    inventory_hostname_short = get_variable(host, "inventory_hostname").split(".")[0]

    config_file_path = f"{operator_user.home}/.ssh/config.d/{sshconfig_order}-{inventory_hostname_short}"
    config_file = host.file(config_file_path)

    assert config_file.exists
    assert config_file.mode == 0o600

    with host.sudo(operator_user_name):
        sshconfig_user = jinja_replacement(
            get_variable(host, "sshconfig_user"), {"operator_user": operator_user_name}
        )
        config_content = host.check_output(f"cat {config_file_path}")
        assert f"Host {inventory_hostname_short}" in config_content
        assert f"User {sshconfig_user}" in config_content
        assert f"Port {get_variable(host, 'sshconfig_port')}" in config_content
        assert (
            f"IdentityFile {get_variable(host, 'sshconfig_private_key_file')}"
            in config_content
        )


def test_sshconfig_files(host):
    operator_user_name = get_variable(host, "operator_user")
    operator_user = host.user(operator_user_name)

    assembled_config = host.file(f"{operator_user.home}/.ssh/config")
    assert assembled_config.exists
    assert assembled_config.user == get_variable(host, "operator_user")
    assert assembled_config.group == get_variable(host, "operator_group")
    assert assembled_config.mode == 0o600

    sshconfig_extra = get_variable(host, "sshconfig_extra")

    if sshconfig_extra != "":
        test_sshconfig_extra = host.file(
            f"{operator_user.home}/.ssh/config.d/999-extra"
        )
        assert test_sshconfig_extra.exists
        assert test_sshconfig_extra.user == get_variable(host, "operator_user")
        assert test_sshconfig_extra.group == get_variable(host, "operator_group")
        assert test_sshconfig_extra.mode == 0o600
        assert "# test content" in test_sshconfig_extra.content_string
