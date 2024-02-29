from .util.util import get_ansible, get_variable, jinja_list_concat

testinfra_runner, testinfra_hosts = get_ansible()


def test_microcode_packages(host):
    microcode_packages_extra = get_variable(host, "microcode_packages_extra")

    if get_variable(host, "ansible_os_family", True) == "Debian":
        microcode_packages_default = get_variable(host, "microcode_packages_default")
        microcode_packages_debian = get_variable(host, "microcode_packages_debian")
        microcode_packages = jinja_list_concat(
            microcode_packages_debian,
            [microcode_packages_default, microcode_packages_extra],
        )
        assert type(microcode_packages) is list
        assert len(microcode_packages) > 0

        for package_name in microcode_packages:
            package = host.package(package_name)
            assert package.is_installed

    if get_variable(host, "ansible_os_family", True) == "RedHat":
        microcode_packages_default = get_variable(host, "microcode_packages_centos")
        microcode_packages_redhat = get_variable(host, "microcode_packages_redhat")

        microcode_packages = jinja_list_concat(
            microcode_packages_redhat,
            [microcode_packages_default, microcode_packages_extra],
        )
        assert type(microcode_packages) is list
        assert len(microcode_packages) > 0

        for package_name in microcode_packages:
            package = host.package(package_name)
            assert package.is_installed
