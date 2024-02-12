from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def check_file_attributes(host, path):
    f = host.file(f"{path}")
    assert f.exists
    assert f.is_directory
    assert f.user == get_variable(host, "configuration_operator_user")
    assert f.group == get_variable(host, "configuration_operator_group")
    assert f.mode == 0o750


def test_folders(host):
    directories = get_variable(host, "configuration_directory")

    if type(directories) is list:
        for d in directories:
            check_file_attributes(host, d)
    elif type(directories) is str:
        assert directories != ""
        check_file_attributes(host, directories)
    else:
        assert False
