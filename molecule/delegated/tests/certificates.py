from .util.util import get_ansible, get_variable, get_family_role_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_files(host):
    certificates = get_variable(host, "certificates_ca")
    path = get_family_role_variable(host, "certificates_ca_path")

    assert type(certificates) is list
    assert path != ""

    for ca_cert in certificates:
        f = host.file(f"{path}/{ca_cert['name']}")
        assert f.exists
        assert f.user == "root"
        assert f.group == "root"
        assert f.mode == 0o644
        assert f.content_string == ca_cert["certificate"]


def test_pkg(host):
    package_name = get_variable(host, "certificates_ca_package_name")
    package = host.package(package_name)

    assert package_name != ""
    assert package.is_installed
