#!/anaconda3/envs/pytorch/bin/python3.7

import shutil
import sys
import os

def check_reboot():
    '''Returns True, if the computer has a pending reboot.'''
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):
    ''' Return True if there isn't enough disk space, False otherwise. '''
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free/du.total
    # Caalculat ehow many free gigabytes
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return True
    return False

	
def check_root_full():
    '''Returns True if the root partition is full, False otherwise. '''
    return check_disk_full("/", min_percent=10, min_gb=2)

def check_cpu_constrained():
    '''Returns True is CPU is having too much usage, False otherwise.'''
    return psutil.cpu_percent(1) > 75


def main():
    checks = [
        (check_reboot, "Pending Reboot"),
        (check_root_full, "Root partition full."),
	(check_cpu_constrained, "CPU Load too high.")
    ]

    everythong_ok = True
    for check, msg in checks:
        if check():
           print(msg)
           everythong_ok = False

    if not everythong_ok:
        sys.exit(1)

    print("Everything ok. ")
    sys.exit(0)

main()
