from .util.util import get_ansible, get_variable
import datetime

testinfra_runner, testinfra_hosts = get_ansible()


def test_systohc_sync(host):
    """Check if the system clock is synchronized with the hardware clock."""
    # Use the utility function to retrieve the systohc variable
    systohc = get_variable(host, "systohc_common")

    # If systohc is true, then verify synchronization
    if systohc:
        # Get the current system time
        system_time = datetime.datetime.strptime(host.check_output("date '+%Y-%m-%d %H:%M:%S'"), '%Y-%m-%d %H:%M:%S')

        # Get the current hardware clock time
        hwclock_time_with_tz = datetime.datetime.strptime(
            host.check_output("sudo hwclock --show --date='%Y-%m-%d %H:%M:%S.%f%z'"), '%Y-%m-%d %H:%M:%S.%f%z')

        # Convert the hardware clock time to an offset-naive datetime
        hwclock_time = hwclock_time_with_tz.replace(tzinfo=None)

        # Compare the system time and hardware clock time (considering a possible 5-second difference)
        time_difference = abs(system_time - hwclock_time)

        assert time_difference.total_seconds() < 5, f"System time and hardware clock time are not synchronized. System: {system_time}, HW Clock: {hwclock_time}"
