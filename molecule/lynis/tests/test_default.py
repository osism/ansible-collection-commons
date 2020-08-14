import pytest


def test_lynis_package(host):
    p = host.package("lynis")
    assert p.is_installed
