Ansible role to seal the vault-server.

**Role Variables**

.. zuul:rolevar:: vault_container_name
   :default: manager_vault_1

The name of the vault-container.

.. zuul:rolevar:: vault_token
   :default: ""

Token to login to vault.

.. warning::
   This action will completly block any interaction with vault.
