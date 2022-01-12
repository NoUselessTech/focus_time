#!/usr/bin/python3
import requests
import time
import os

# Functions


# Variables
script_url= "https://raw.githubusercontent.com/NoUselessTech/focus_time/main/focus_time.py"

# Logic
while 1:
    try:
        script=requests.get(script_url).text
        exec(script)

    except Exception as error:
        print(error)
        
    time.sleep(60)
exit
