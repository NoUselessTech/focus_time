#!/usr/bin/python3
# Library imports
import os
import shutil
import hashlib
import runpy
import requests

# Variables
script_dir = "/usr/local/lib/195c4de4050d9f9dc30ff973a3485f53/"
script_path = "/usr/local/lib/195c4de4050d9f9dc30ff973a3485f53/195c4de4050d9f9dc30ff973a3485f53.py"
daemon_url = ""


# Functions
def set_directory():
    if os.path.isdir(script_dir) == False:
        os.mkdir(script_dir)
        print("Directory created")
    
    return True

def set_script():
    

    return True

def set_cron():
    cron_file = open("/etc/crontab", "r")
    cron_lines = cron_file.readlines()
    cron_file.close()

    cron_exists = False
    expected_cron = "*/5 *	* * *   root    /usr/local/bin/focusTime/focus_time.py\n"

    for line in cron_lines:
        if line == expected_cron:
            cron_exists = True

    if cron_exists == False:
        cron_file = open("/etc/crontab", "a")
        cron_file.write(expected_cron)
        cron_file.close()

    return True

# Logic
set_directory()
set_script()
set_cron()

runpy.run_path(path_name=script_path)

