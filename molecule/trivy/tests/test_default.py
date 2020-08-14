import pytest


def test_trivy_package(host):
    p = host.package("trivy")
    assert p.is_installed
