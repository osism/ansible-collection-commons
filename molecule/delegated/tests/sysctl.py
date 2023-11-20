from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_sysctl_settings(host):
    group_names = get_variable(host, "group_names")
    sysctl_defaults = get_variable(host, "sysctl_defaults")
    sysctl_extra = get_variable(host, "sysctl_extra")

    sysctl_config = sysctl_defaults.copy()
    sysctl_config.update(sysctl_extra)

    for key, settings in sysctl_config.items():
        if key not in group_names:
            continue

        assert host.file("/etc/sysctl.d/70-{key}.conf").exists

        for setting in settings:
            sysctl_name = setting["name"]
            expected_value = str(setting["value"])

            sysctl_path = f"/proc/sys/{sysctl_name.replace('.', '/')}"

            if host.file(sysctl_path).exists:
                actual_value = host.file(sysctl_path).content_string.strip()
                assert actual_value == expected_value
