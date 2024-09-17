from ..util.util import get_ansible, get_variable, get_family_role_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_dropbear_artifacts_removed(host):
    dropbear_conf = host.file("/etc/initramfs-tools/conf.d/dropbear.conf")
    assert not dropbear_conf.exists


def test_clevis_packages(host):
    clevis_packages = get_family_role_variable(host, "clevis_packages")

    for package_name in clevis_packages:
        package = host.package(package_name)
        assert package.is_installed


def test_clevis_service_enabled(host):
    clevis_service = get_variable(host, "clevis_service_name")
    service = host.service(clevis_service)
    assert service.is_enabled
