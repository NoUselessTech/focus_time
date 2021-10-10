#!/usr/bin/python3
import requests
import time

# Functions


# Variables
script_location= "https://raw.githubusercontent.com/Angretlam/focus_time/main/focus_time.py"

# Logic

while 1:
    try:
        script=requests.get(script_location).text
        exec(script)
        print("Successfully set productivity boosts.\n")

    except:
        print("Unable to run script. Likely due to network issues.\n")
        
    time.sleep(300)
exit