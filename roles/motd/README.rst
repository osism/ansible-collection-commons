Sets the content of the Message of the Day (MOTD) file.

**Role Variables**

.. zuul:rolevar:: motd_content
   :default: ""

   Contents to be written to ``motd_path``.

   Example:

   .. code-block:: yaml

      motd_content: |
        ------------------------------------------------------------------------------
        * WARNING                                                                    *
        * You are accessing a secured system and your actions will be logged along   *
        * with identifying information. Disconnect immediately if you are not an     *
        * authorized user of this system.                                            *
        ------------------------------------------------------------------------------

.. zuul:rolevar:: motd_path
   :default: /etc/motd

   The full path to the motd file.
