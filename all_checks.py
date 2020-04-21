#!/anaconda3/envs/pytorch/bin/python3.7

import shutil
import sys
import os

def check_reboot():
    '''Returns True, if the computer has a pending reboot.'''
    return os.path.exists("/run/reboot-required")

def check_disk_usage(disk, min_gb, min_percent):
    du = shutil.disk_usage(disk)
    percent_free = 100 * du.free/du.total
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return False
    return True

if not check_disk_usage("/", min_percent = 10, min_gb = 2):
    print("ERROR : Not enough disk space.!")
    sys.exit(1)

print("Everything ok. ")
sys.exit(0)
