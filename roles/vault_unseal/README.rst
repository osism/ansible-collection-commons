Ansible role to unseal the vault-server.

**Role Variable**

.. zuul:rolevar:: vault_container_name
   :default: manager_vault_1

The name from the vault-container to interact with it.

The algorithm to unseal the vault-server is called shamir.
For the unsealing you will need at least three keys:

.. zuul:rolevar:: vault_unseal_key_1

.. zuul:rolevar:: vault_unseal_key_2

.. zuul:rolevar:: vault_unseal_key_3
