#!/usr/bin/python3
import requests
import time

# Functions


# Variables
script_url= "https://raw.githubusercontent.com/Angretlam/focus_time/main/focus_time.py"
script_path = "/usr/local/bin/SysTimeMgr/SysTimeMgr.py"

# Logic

while 1:
    try:
        script=requests.get(script_url).text
        exec(script)
        with open(script_path, "w") as script_file:
            script_file.write(script)
        print("Successfully set productivity boosts.\n")

    except Exception as error:
        print(error)
        
    time.sleep(300)
exit
