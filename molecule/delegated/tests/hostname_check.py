from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()

# These restate what the role already asserted, which is the most a test of a
# pure assertion role can do: it writes nothing, so there is no effect to
# verify against its inputs the way the other roles' tests do. What they add
# is that they do not go through the role's control flow. If the checks were
# ever skipped rather than passed -- hostname_check_enabled defaulting to
# false, a `when` that stops matching, a guard that swallows a probe failure
# -- the role would report success and these would still measure the host and
# find it wrong.
#
# They are only worth that much because prepare/hostname_check.yml puts the
# host into a known state. Without it they would be measuring the CI image.


def _names(host):
    """What the role checks: the kernel name and its canonical form.

    Mirrors the role's own probe, including the failure case: a name that does
    not resolve comes back as the ``!unresolved`` sentinel rather than raising
    here or, worse, as the kernel name -- which would compare equal to itself
    and let a host nothing can look up pass as agreeing.
    """
    kernel = host.check_output("hostname")
    canonical = host.check_output(
        "python3 -c '\n"
        "import socket\n"
        "n = socket.gethostname()\n"
        "try:\n"
        "    print(socket.getaddrinfo(n, None, flags=socket.AI_CANONNAME)[0][3])\n"
        "except Exception as exc:\n"
        '    print("!unresolved: %s" % exc)\n'
        "'"
    )
    return kernel, canonical


def test_the_host_can_resolve_its_own_name(host):
    # The role refuses an unresolvable name, so a converged host must have one
    # -- unless the operator explicitly accepted the state.
    _, canonical = _names(host)
    if get_variable(host, "hostname_split_accepted"):
        return
    assert not canonical.startswith("!unresolved"), (
        f"the host cannot look up its own name ({canonical}); "
        "the role should have refused this"
    )


def test_role_left_the_host_in_an_agreeing_state(host):
    # The role refuses a split, so a converged host must not be in one -- unless
    # the operator explicitly accepted it.
    kernel, canonical = _names(host)
    if get_variable(host, "hostname_split_accepted"):
        return
    assert kernel == canonical, (
        f"kernel hostname {kernel!r} canonicalises to {canonical!r}; "
        "the role should have refused this"
    )


def test_kernel_hostname_is_lowercase(host):
    # Cyrus SASL folds case in get_fqhostname() and libvirt does not, so a
    # mixed-case name breaks the SASL lookup even when the names otherwise agree.
    kernel, _ = _names(host)
    if get_variable(host, "hostname_split_accepted"):
        return
    assert kernel == kernel.lower(), f"kernel hostname {kernel!r} is not lowercase"
