#!/usr/bin/env bash

# usage: bash scripts/generate-job-workflows.sh

# requirements: pip3 install jinja-cli

for role in cleanup configuration facts hostname kompose kubectl microcode motd operator packages podman proxy repository resolvconf services sshconfig state sysctl systohc trivy timezone; do
  jinja -D ansible_role $role \
        -D ansible_versions "['4.2.0']" \
        -D python_versions "['3.8']" \
        -D docker_images "['ubuntu:20.04']" \
        -D molecule_scenario "default" \
    templates/test-role.yml.j2 > workflows/test-role-$role.yml
done

for role in configfs sysdig lynis ipmitool kernel_modules firewall; do
  jinja -D ansible_role $role \
        -D ansible_versions "['4.2.0']" \
        -D python_versions "['3.8']" \
        -D docker_images "['ubuntu:20.04']" \
        -D molecule_scenario "delegated" \
    templates/test-role.yml.j2 > workflows/test-role-$role.yml
done
