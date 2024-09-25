from ..util.util import get_ansible

testinfra_runner, testinfra_hosts = get_ansible()


def test_function(host):
    with host.sudo():
        result = host.run("lynis audit system --quick")
        assert result.rc == 0
        assert "check" in result.stdout.lower()
