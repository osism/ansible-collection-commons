# Ansible collection osism.commons

Documentation: https://osism.github.io/docs/guides/configuration-guides/commons/

The following Ansible roles are included in this collection.

| Rolename       | Molecule Unit Tests                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| certificates   | [certificates.py](molecule/delegated/tests/certificates.py)                                                                                                                                                                                                                                                                                                                                                                                                                            |
| cleanup        | [cloudinit.py](molecule/delegated/tests/cleanup/cloudinit.py) <br/>[packages.py](molecule/delegated/tests/cleanup/packages.py) <br/>[cloudinit.py](molecule/delegated/tests/cleanup/cloudinit.py) <br/>[packages_debian.py](molecule/delegated/tests/cleanup/packages_debian.py) <br/>[services.py](molecule/delegated/tests/cleanup/services.py) <br/>[timer_debian.py](molecule/delegated/tests/cleanup/timer_debian.py) <br/>[timer_redhat.py](molecule/delegated/tests/cleanup/timer_redhat.py) |
| configfs       | [configfs.py](molecule/delegated/tests/configfs.py)                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| configuration  | [git.py](molecule/delegated/tests/configuration/git.py)<br/> [main.py](molecule/delegated/tests/configuration/main.py)                                                                                                                                                                                                                                                                                                                                                                 |
| docker_compose | [docker_compose.py](molecule/delegated/tests/docker_compose.py)                                                                                                                                                                                                                                                                                                                                                                                                                        |
| docker_login   | [docker_login.py](molecule/delegated/tests/docker_login.py)                                                                                                                                                                                                                                                                                                                                                                                                                            |
| facts          | [facts.py](molecule/delegated/tests/facts.py)                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| firewall       | [firewall.py](molecule/delegated/tests/firewall.py)                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| hostname       | [hostname.py](molecule/delegated/tests/hostname.py)                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| hosts          | [type-block.py](molecule/delegated/tests/hosts/type-block.py) <br/>[type-template.py](molecule/delegated/tests/hosts/type-template.py)                                                                                                                                                                                                                                                                                                                                                 |
| ipmitool       | [ipmitool.py](molecule/delegated/tests/ipmitool.py)                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| kernel_modules | [kernel_modules.py](molecule/delegated/tests/kernel_modules.py)                                                                                                                                                                                                                                                                                                                                                                                                                        |
| known_hosts    | [known_hosts.py](molecule/delegated/tests/known_hosts.py)                                                                                                                                                                                                                                                                                                                                                                                                                              |
| kompose        | [main.py](molecule/delegated/tests/kompose/main.py) <br/>[debian.py](molecule/delegated/tests/kompose/debian.py) <br/>[redhat.py](molecule/delegated/tests/kompose/redhat.py)                                                                                                                                                                                                                                                                                                          |
| kubectl        | [main.py](molecule/delegated/tests/kubectl/main.py) <br/>[debian.py](molecule/delegated/tests/kubectl/debian.py) <br/>[redhat.py](molecule/delegated/tests/kubectl/redhat.py)                                                                                                                                                                                                                                                                                                          |
| limits         | [limits.py](molecule/delegated/tests/limits.py)                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| lynis          | [debian.py](molecule/delegated/tests/lynis/debian.py) <br/>[redhat.py](molecule/delegated/tests/lynis/redhat.py)                                                                                                                                                                                                                                                                                                                                                                       |
| microcode      | [microcode.py](molecule/delegated/tests/microcode.py)                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| motd           | [main.py](molecule/delegated/tests/motd/main.py) <br/>[debian.py](molecule/delegated/tests/motd/debian.py)                                                                                                                                                                                                                                                                                                                                                                             |
| network        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| operator       | [operator.py](molecule/delegated/tests/operator.py)                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| packages       | [main.py](molecule/delegated/tests/packages/main.py) <br/>[debian.py](molecule/delegated/tests/packages/debian.py) <br/>[redhat.py](molecule/delegated/tests/packages/redhat.py)                                                                                                                                                                                                                                                                                                       |
| podman         | [podman.py](molecule/delegated/tests/podman)                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| proxy          | [main.py](molecule/delegated/tests/proxy/main.py) <br/>[debian.py](molecule/delegated/tests/proxy/main.py) <br/>[redhat.py](molecule/delegated/tests/proxy/redhat.py)                                                                                                                                                                                                                                                                                                                  |
| repository     | [ubuntu.py](molecule/delegated/tests/repository/ubuntu.py) <br/>[centos.py](molecule/delegated/tests/repository/centos.py)                                                                                                                                                                                                                                                                                                                                                             |
| resolvconf     | [resolvconf.py](molecule/delegated/tests/resolvconf.py)                                                                                                                                                                                                                                                                                                  |
| runc           | [runc.py](molecule/delegated/tests/runc.py)                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| services       | [services.py](molecule/delegated/tests/services.py)                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| sosreport      | [sosreport.py](molecule/delegated/tests/sosreport.py)                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| sshconfig      | [sshconfig.py](molecule/delegated/tests/sshconfig.py)                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| state          | [state.py](molecule/delegated/tests/state.py)                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| sysctl         | [sysctl.py](molecule/delegated/tests/sysctl.py)                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| systohc        | [systohc.py](molecule/delegated/tests/systohc.py)                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| timezone       | [main.py](molecule/delegated/tests/timezone/main.py) <br/>[debian.py](molecule/delegated/tests/timezone/debian.py) <br/>[rehat.py](molecule/delegated/tests/timezone/redhat.py)                                                                                                                                                                                                                                                                                                        |
| trivy          | [debian.py](molecule/delegated/tests/trivy/debian.py) <br/>[redhat.py](molecule/delegated/tests/trivy/redhat.py)                                                                                                                                                                                                                                                                                                                                                                       |
| user           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
