from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_limits_set_correctly(host):
    # Fetching the variables from Ansible
    limits_defaults = get_variable(host, "limits_defaults")
    limits_extra = get_variable(host, "limits_extra")
    combined_limits = {**limits_defaults, **limits_extra}

    # Mapping of limit types to ulimit options
    ulimit_options = {
        "hard": "H",
        "soft": "S",
        # add other mappings as needed
    }

    for domain, limits in combined_limits.items():
        for limit in limits:
            ulimit_option = ulimit_options.get(limit["type"], None)
            if ulimit_option:
                # Fetching the current domain's limits using ulimit
                result = host.check_output(f"ulimit -a -{ulimit_option}")

                # Parsing the ulimit output to get the limit value
                for line in result.split("\n"):
                    item, value = line.split()[:2]
                    if item == limit["item"]:
                        # Asserting if the limit has been set correctly
                        assert int(value) == int(limit["value"])
                        break


def test_limits_files_exist(host):
    # Just a sample to check if the files related to limits exist on the system
    # Modify as per your requirements
    f = host.file("/etc/security/limits.conf")
    assert f.exists
    assert not f.is_directory
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o644
