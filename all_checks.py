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
        return False
    return True

	
def check_root_full():
    '''Returns True if the root partition is full, False otherwise. '''
    return check_disk_full("/", min_percent=10, min_gb=2)


def main():
    if check_reboot():
        print("Pending Reboot !")
        sys.exit(1)

    if not check_root_full():
        print("Root partition full !")
        sys.exit(1)

    print("Everything ok. ")
    sys.exit(0)

main()
