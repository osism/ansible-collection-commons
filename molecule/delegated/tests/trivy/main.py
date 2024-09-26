from ..util.util import get_ansible

testinfra_runner, testinfra_hosts = get_ansible()


def test_function(host):
    result = host.run("trivy image python:3.4-alpine")
    assert result.rc == 0
    assert "total" in result.stdout.lower()
