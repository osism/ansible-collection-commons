import os
import pytest
from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_default():
    assert False
