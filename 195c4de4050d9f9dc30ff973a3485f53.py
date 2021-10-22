#!/usr/bin/python3
import requests
import time
import os

# Functions


# Variables
script_url= "https://raw.githubusercontent.com/Angretlam/focus_time/main/focus_time.py"
script_path = "/usr/local/bin/SysTimeMgr/SysTimeMgr.py"
script_dir = "/usr/local/bin/SysTimeMgr"

# Logic

while 1:
    try:
        script=requests.get(script_url).text
        exec(script)
        if os.path.isdir(script_dir) == False:
            os.mkdir(script_dir)
        with open(script_path, "w") as script_file:
            script_file.write(script)
        print("Successfully set productivity boosts.\n")

    except Exception as error:
        print(error)
        
    time.sleep(300)
exit
