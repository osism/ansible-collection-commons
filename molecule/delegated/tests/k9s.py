def test_runc_package(host):
    package = host.package("k9s")
    assert package.is_installed
