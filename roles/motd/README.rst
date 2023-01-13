Sets the content of the Message of the Day (/etc/motd) and the
prelogin message and identification (/etc/issue) file.

**Role Variables**

.. zuul:rolevar:: motd_content
   :default: ""

   Contents to be written to ``motd_path`` and ``issue_path``.

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

.. zuul:rolevar:: issue_path
   :default: /etc/issue

   The full path to the issue file.
