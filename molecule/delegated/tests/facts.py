from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_custom_facts_directory(host):
    facts_dir = host.file('/etc/ansible/facts.d')

    assert facts_dir.exists
    assert facts_dir.is_directory
    assert facts_dir.user == "root"
    assert facts_dir.group == "root"
    assert facts_dir.mode == 0o755


def test_fact_files(host):
    fact_files = get_variable(host, 'fact_files')

    assert type(fact_files) is list

    for fact_file in fact_files:
        f = host.file(f'/etc/ansible/facts.d/{fact_file}.fact')

        assert f.exists
        assert f.user == "root"
        assert f.group == "root"
        assert f.mode == 0o755
