import os
import testinfra.utils.ansible_runner

def get_ansible():
    testinfra_runner = testinfra.utils.ansible_runner.AnsibleRunner(
        os.environ['MOLECULE_INVENTORY_FILE'])
    testinfra_hosts = testinfra_runner.get_hosts('all')

    return testinfra_runner, testinfra_hosts

def get_variable(host, name):
    all_vars = host.ansible.get_variables()
    if name in all_vars:
        return all_vars[name]

    #debug_value = host.ansible("debug", f"var={name}")[name]
    #if not debug_value.startswith('VARIABLE IS NOT DEFINED!'):
    #    return debug_value

    role_name = os.environ["ROLE_NAME"]

    test_vars = host.ansible("include_vars", f"../../molecule/delegated/vars/{role_name}.yml")["ansible_facts"]
    if name in test_vars:
        return test_vars[name]

    default_vars = host.ansible("include_vars", f"../../roles/{role_name}/defaults/main.yml")["ansible_facts"]
    if name in default_vars:
        return default_vars[name]

    raise Exception(f"Variable {name} not found!")
