# SPDX-License-Identifier: GPL-3.0-or-later

import sys
from threading import Thread
import time

from ansible.plugins.callback.default import CallbackModule as Default


__metaclass__ = type

DOCUMENTATION = """
    author: Christian Berendt
    name: still_alive
    type: stdout
    short_description: Display an still alive message every 30 seconds
    description: Display an still alive message every 30 seconds
    extends_documentation_fragment:
      - default_callback
    requirements:
      - set as stdout in configuration
"""


class CallbackModule(Default):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = "stdout"
    CALLBACK_NAME = "osism.commons.still_alive"

    DELAY = 30
    TIMEOUT = 120

    def display_still_alive(self):
        while True:
            time.sleep(self.DELAY)
            if (
                not self.skip
                and self.task_name
                and time.time() - self.last >= self.TIMEOUT
            ):
                self._display.banner(
                    f"STILL ALIVE [task '{self.task_name}' is running]"
                )
                sys.stdout.flush()

    def __init__(self):
        super(CallbackModule, self).__init__()
        self.t = Thread(target=self.display_still_alive, daemon=True)
        self.t.start()

        self.last = time.time()
        self.skip = False
        self.task_name = None

    def v2_runner_on_failed(self, result, ignore_errors=False):
        self.last = time.time()
        super().v2_runner_on_failed(result, ignore_errors)

    def v2_runner_on_ok(self, result):
        self.last = time.time()
        super().v2_runner_on_ok(result)

    def v2_playbook_on_start(self, playbook):
        self.last = time.time()
        self.skip = False
        super().v2_playbook_on_start(playbook)

    def v2_playbook_on_task_start(self, task, is_conditional):
        self.last = time.time()
        self.task_name = task.get_name().strip()
        super().v2_playbook_on_task_start(task, is_conditional)

    def v2_playbook_on_stats(self, stats):
        self.skip = True
        super().v2_playbook_on_stats(stats)
