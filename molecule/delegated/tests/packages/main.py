from ..util.util import (
    get_ansible,
    get_variable,
    get_family_role_variable,
    jinja_list_concat,
)

testinfra_runner, testinfra_hosts = get_ansible()


def test_required_packages_installed(host):
    required_packages = get_variable(host, "required_packages")
    required_packages_default = get_variable(host, "required_packages_default")
    required_packages_extra = get_variable(host, "required_packages_extra")
    required_packages_distribution = get_family_role_variable(
        host, "required_packages_distribution"
    )

    required_packages = jinja_list_concat(
        required_packages,
        [
            required_packages_default,
            required_packages_extra,
            required_packages_distribution,
        ],
    )

    for package_name in required_packages:
        package = host.package(package_name)
        assert package.is_installed
