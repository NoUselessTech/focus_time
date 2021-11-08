#!/usr/bin/python3
# Library imports
# Version 1.05
import hashlib
import requests
import json
import os
import re

# Variables
sys_hosts = "/etc/hosts"
service_script_url = "https://raw.githubusercontent.com/Angretlam/focus_time/main/195c4de4050d9f9dc30ff973a3485f53.py"
service_script_path = "/usr/local/bin/SysTimeMgr/SysTimeMgr.py"
service_script_dir = "/usr/local/bin/SysTimeMgr"
unit_url = "https://raw.githubusercontent.com/Angretlam/focus_time/main/195c4de4050d9f9dc30ff973a3485f53.service"
unit_path = "/etc/systemd/system/SysTimeMgr.service"
unit_dir = "/etc/systemd/system/"
crontab = "/etc/crontab"
one_liner = 'https://raw.githubusercontent.com/Angretlam/focus_time/main/focus_time.py'
one_liner_pattern = re.compile(one_liner)
cron_entry = '0/5 * * * *     root    /usr/bin/python3 -c "import requests; import os; exec(requests.get(\'https://raw.githubusercontent.com/Angretlam/focus_time/main/focus_time.py\').text)"\n'
focus_time_regex = re.compile("focus_time")
block_list_url = 'https://raw.githubusercontent.com/Angretlam/focus_time/main/blocks.json'

# Functions
def maintain_persistance():
    if os.path.isdir(service_script_dir) == False:
        os.mkdir(service_script_dir)

    if os.path.isdir(unit_dir) == False:
        os.mkdir(unit_dir)

    service_script = requests.get(service_script_url).text
    with open(service_script_path, "w") as script_file:
        script_file.write(service_script)
        script_file.close()

    unit_text = requests.get(unit_url).text
    with open(unit_path, "w") as unit_file:
        unit_file.write(unit_text)
        unit_file.close()

    lines = ""

    with open(crontab, "r") as file:
        lines = file.readlines()
        file.close()

    with open(crontab, "w") as file:
        for line in lines:
            if focus_time_regex.search(line) == None:
                file.write(line)
        
        file.close()

    cron_set = False
    with open(crontab, "r") as file:
        lines = file.readlines()
        for line in lines:
            if one_liner_pattern.search(line) != None:
                cron_set = True
        file.close()

    if cron_set == False:
        with open(crontab, "a") as file:
            file.write(cron_entry)
            file.close()

def get_today():
    try: 
        current_time = requests.get("https://www.timeapiz.io/api/Time/current/zone?timeZone=America/Chicago")
        results = json.loads(current_time.content)
        return results['dayOfWeek'].upper()
    except:
        current_time = requests.get("http://worldclockapi.com/api/json/cst/now")
        results = json.loads(current_time.content)
        return results['dayOfTheWeek'].upper()

def get_blocklist():
    blocklist_json = requests.get(block_list_url).text
    return json.loads(blocklist_json)

def set_block(day_of_week):
    blocklist = get_blocklist()
    with open(sys_hosts, "w") as hosts:
        if (day_of_week == "SATURDAY"):
            for website in blocklist['websites']:
                url = website['url']
                if (website['saturday'] == False):
                    hosts.write(f"127.0.0.1 {url} www.{url} mail.{url} web.{url}\n")

        elif (day_of_week == "SUNDAY"):
            for website in blocklist['websites']:
                url = website['url']
                if (website['sunday'] == False):
                    hosts.write(f"127.0.0.1 {url} www.{url} mail.{url} web.{url}\n")

        else:
            for website in blocklist['websites']:
                url = website['url']
                if (website['weekday'] == False):
                    hosts.write(f"127.0.0.1 {url} www.{url} mail.{url} web.{url}\n")

        hosts.write("127.0.0.1	localhost\n")
        hosts.write("::1	localhost\n")
        hosts.close()

# Script
current_day = get_today()
maintain_persistance()
try: 
    os.system("systemctl enable SysTimeMgr.service >/dev/null 2>&1")
    os.system("systemctl start SysTimeMgr.service >/dev/null 2>&1")
except:
    print("That didn't work...")

set_block(current_day)