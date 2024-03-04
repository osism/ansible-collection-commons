# Ansible collection osism.commons

Documentation: https://osism.github.io/docs/guides/configuration-guides/commons/

The following Ansible roles are included in this collection.

| Rolename       | Molecule Unit Tests                                                                                                                                                   |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| certificates   | [certificates](molecule/delegated/tests/certificates)                                                                                                                 |
| cleanup        | [cleanup](molecule/delegated/tests/cleanup)                                                                                                                           |
| configfs       | [configfs.py](molecule/delegated/tests/configfs.py)                                                                                                                   |
| configuration  | [configuration](molecule/delegated/tests/configuration)                                                                                                               |
| docker_compose | [docker_compose.py](molecule/delegated/tests/docker_compose.py)                                                                                                       |
| docker_login   | [docker_login.py](molecule/delegated/tests/docker_login.py)                                                                                                           |
| facts          | [facts.py](molecule/delegated/tests/facts.py)                                                                                                                         |
| firewall       | [firewall.py](molecule/delegated/tests/firewall.py)                                                                                                                   |
| hostname       | [hostname.py](molecule/delegated/tests/hostname.py)                                                                                                                   |
| hosts          | [hosts](molecule/delegated/tests/hosts)                                                                                                                               |
| ipmitool       | [ipmitool.py](molecule/delegated/tests/ipmitool.py)                                                                                                                   |
| kernel_modules | [kernel_modules.py](molecule/delegated/tests/kernel_modules.py)                                                                                                       |
| known_hosts    | [known_hosts.py](molecule/delegated/tests/known_hosts.py)                                                                                                             |
| kompose        | [kompose.py](molecule/delegated/tests/kompose)                                                                                                                        |
| kubectl        | [main.py](molecule/delegated/tests/kubectl/main.py), [debian.py](molecule/delegated/tests/kubectl/debian.py), [redhat.py](molecule/delegated/tests/kubectl/redhat.py) |
| limits         | [limits.py](molecule/delegated/tests/limits.py)                                                                                                                       |
| lynis          | [lynis.py](molecule/delegated/tests/lynis)                                                                                                                            |
| microcode      | [microcode.py](molecule/delegated/tests/microcode.py)                                                                                                                 |
| motd           | [motd](molecule/delegated/tests/motd)                                                                                                                                 |
| network        | [network](molecule/delegated/tests/network)                                                                                                                           |
| operator       | [operator.py](molecule/delegated/tests/operator.py)                                                                                                                   |
| packages       | [packages](molecule/delegated/tests/packages)                                                                                                                         |
| podman         | [podman.py](molecule/delegated/tests/podman)                                                                                                                          |
| proxy          | [proxy](molecule/delegated/tests/proxy)                                                                                                                               |
| repository     | [repository](molecule/delegated/tests/repository)                                                                                                                     |
| resolvconf     | [resolvconf.py](molecule/delegated/tests/resolvconf)                                                                                                                  |
| runc           | [runc.py](molecule/delegated/tests/runc.py)                                                                                                                           |
| services       | [services.py](molecule/delegated/tests/services.py)                                                                                                                   |
| sosreport      | [sosreport.py](molecule/delegated/tests/sosreport.py)                                                                                                                 |
| sshconfig      | [sshconfig.py](molecule/delegated/tests/sshconfig.py)                                                                                                                 |
| state          | [state.py](molecule/delegated/tests/state.py)                                                                                                                         |
| sysctl         | [sysctl.py](molecule/delegated/tests/sysctl.py)                                                                                                                       |
| systohc        | [systohc.py](molecule/delegated/tests/systohc.py)                                                                                                                     |
| timezone       | [timezone.py](molecule/delegated/tests/timezone)                                                                                                                      |
| trivy          | [debian.py](molecule/delegated/tests/trivy/debian.py), [redhat.py](molecule/delegated/tests/trivy/redhat.py)                                                          |
