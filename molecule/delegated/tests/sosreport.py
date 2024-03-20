from .util.util import (
    get_ansible,
    get_variable,
    jinja_replacement,
    get_family_role_variable,
)

testinfra_runner, testinfra_hosts = get_ansible()


def test_required_packages_installed(host):
    required_packages = get_family_role_variable(host, "sosreport_required_packages")

    for package_name in required_packages:
        package = host.package(package_name)
        assert package.is_installed, f"Package {package_name} should be installed"


def test_report_generation(host):
    # Construct the directory
    sosreport_archive_directory = get_variable(host, "sosreport_archive_directory")
    current_date = host.check_output("date +%Y-%m-%d")
    sosreport_archive_directory = jinja_replacement(
        sosreport_archive_directory,
        {"ansible_date_time": type("obj", (), {"date": current_date})},
    )

    # Construct the filename
    inventory_hostname = get_variable(host, "inventory_hostname")
    inventory_hostname_short = inventory_hostname.split(".")[0]
    sosreport_name = get_variable(host, "sosreport_name")
    sosreport_name = jinja_replacement(
        sosreport_name,
        {
            "ansible_date_time": type("obj", (), {"date": current_date}),
            "inventory_hostname_short": inventory_hostname_short,
        },
    )
    sosreport_archive_filename = get_variable(host, "sosreport_archive_filename")
    sosreport_archive_filename = jinja_replacement(
        sosreport_archive_filename,
        {"sosreport_name": sosreport_name},
    )

    sosreport_path = sosreport_archive_directory + "/" + sosreport_archive_filename

    # Check if the sosreport file exists
    f = host.file(sosreport_path)
    assert f.exists, f"sosreport file {sosreport_path} does not exist"
    assert not f.is_directory
