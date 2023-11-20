from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_custom_facts_directory(host):
    custom_facts_dir = "/etc/ansible/facts.d"
    file = host.file(custom_facts_dir)

    assert file.exists
    assert file.is_directory
    assert file.user == "root"
    assert file.group == "root"
    assert file.mode == 0o755


def test_state_file(host):
    state_name = get_variable(host, "state_name")
    state_section = get_variable(host, "state_section")
    state_option = get_variable(host, "state_option")
    state_value = get_variable(host, "state_value")

    state_file_path = f"/etc/ansible/facts.d/{state_name}.fact"
    file = host.file(state_file_path)

    assert file.exists
    assert file.user == "root"
    assert file.group == "root"
    assert file.mode == 0o644

    assert f"[{state_section}]" in file.content_string
    assert f"{state_option} = {state_value}" in file.content_string
