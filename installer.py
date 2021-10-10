#!/usr/bin/python3
# Library imports
import os
import shutil
import hashlib
import runpy

# Variables
script_dir = "/usr/local/bin/focusTime/"
script_path = "/usr/local/bin/focusTime/focus_time.py"

# Functions
def set_directory():
    if os.path.isdir(script_dir) == False:
        os.mkdir(script_dir)
        print("Directory created")
    
    return True

def set_script():
    if os.path.isfile(script_path) == False:
        shutil.move("./focus_time.py", script_path)
        print("Fresh install")

    elif os.path.isfile(script_path) == True:
        current_hash = hashlib.md5(open(script_path, "rb").read()).hexdigest();
        new_hash = hashlib.md5(open("./focus_time.py", "rb").read()).hexdigest();
        if current_hash != new_hash:
            os.remove(script_path)
            shutil.move("./focus_time.py", script_path)

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

