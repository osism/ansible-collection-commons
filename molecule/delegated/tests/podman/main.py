import pytest
from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_podman_pkg(host):
    package_name = get_variable(host, "podman_package_name")
    assert package_name != ""

    package = host.package(package_name)
    assert package.is_installed


@pytest.mark.parametrize(
    "name,image,expected_output",
    [("podman_test", "docker.io/hello-world:latest", "Hello from Docker!")],
)
def test_podman_installation(host, name, image, expected_output):
    # Check Podman version
    podman_version = host.run("podman --version")
    assert podman_version.rc == 0
    assert "podman version" in podman_version.stdout.lower()

    # Run a test container
    with host.sudo():
        container = host.run(f"podman run --name {name} {image}")
    assert container.rc == 0
    assert expected_output in container.stdout

    # Check if podman can list images
    list_images = host.run("podman images")
    assert list_images.rc == 0
