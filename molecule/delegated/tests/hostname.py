from .util.util import get_ansible

testinfra_runner, testinfra_hosts = get_ansible()

def test_hostname_settings(host):
    # Fetch system's hostname using the 'hostname' command
    system_hostname = host.check_output('hostname')

    # Verify the /etc/hostname file
    etc_hostname = host.file('/etc/hostname')
    assert etc_hostname.exists
    assert etc_hostname.content_string.strip() == system_hostname
    assert etc_hostname.user == 'root'
    assert etc_hostname.group == 'root'
    assert oct(etc_hostname.mode) == '0o644'
