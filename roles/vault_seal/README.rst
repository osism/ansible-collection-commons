Ansible role to seal the vault-server.

**Role Variable**

.. zuul:rolevar:: vault_container_name
   :default: manager_vault_1

The name from the vault-container to interact with it.

.. zuul:rolevar:: vault_token
   :default: ""

Token to login to vault.

.. code-block:: yaml

        ---------------------------------------------------------------------
        * WARNING                                                           *
        * This action will completly block any interaction with vault.      *
        ---------------------------------------------------------------------