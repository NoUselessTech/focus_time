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

    

def otherdays_blocker():
    # open ONLY saturday
    # https://www.bitchute.com/ done
    # https://odysee.com/ done
    # https://rumble.com/ done
    # https://prayingmedic.com/ done
    # https://t.me/ done
    # https://americafirst.live/ done
    # https://nicholasjfuentes.com/ done
    # https://cozy.tv/ done
    # https://www.instagram.com/ done
    # https://mailfence.com/ done
    # http://rooshv.com/ done
    # open NEVER
    # https://dailystormer.su/ done
    # https://feedly.com/ done
    # http://innercirclex.com/ done
    # https://www.rooshvforum.com/ done
    # https://twitter.com/ done
    # http://gab.com/ done
    # https://9gag.com/ done
    # https://www.facebook.com/ done

    hosts_file = open(sys_hosts, "w")
    hosts_file.write("127.0.0.1	facebook.com\n")
    hosts_file.write("127.0.0.1	www.facebook.com\n")
    hosts_file.write("127.0.0.1	cozy.tv\n")
    hosts_file.write("127.0.0.1	www.cozy.tv\n")
    hosts_file.write("127.0.0.1	mailfence.com\n")
    hosts_file.write("127.0.0.1	www.mailfence.com\n")
    hosts_file.write("127.0.0.1	instagram.com\n")
    hosts_file.write("127.0.0.1	www.instagram.com\n")
    hosts_file.write("127.0.0.1	nicholasjfuentes.com\n")
    hosts_file.write("127.0.0.1	www.nicholasjfuentes.com\n")
    hosts_file.write("127.0.0.1	feedly.com\n")
    hosts_file.write("127.0.0.1	www.feedly.com\n")
    hosts_file.write("127.0.0.1	bitchute.com\n")
    hosts_file.write("127.0.0.1	www.bitchute.com\n")
    hosts_file.write("127.0.0.1	9gag.com\n")
    hosts_file.write("127.0.0.1	www.9gag.com\n")
    hosts_file.write("127.0.0.1	innercirclex.com\n")
    hosts_file.write("127.0.0.1	www.innercirclex.com\n")
    hosts_file.write("127.0.0.1	rooshvforum.com\n")
    hosts_file.write("127.0.0.1	www.rooshvforum.com\n")
    hosts_file.write("127.0.0.1	rooshv.com\n")
    hosts_file.write("127.0.0.1	www.rooshv.com\n")
    hosts_file.write("127.0.0.1	odysee.com\n")
    hosts_file.write("127.0.0.1	www.odysee.com\n")
    hosts_file.write("127.0.0.1	t.me\n")
    hosts_file.write("127.0.0.1	www.t.me\n")
    hosts_file.write("127.0.0.1	prayingmedic.com\n")
    hosts_file.write("127.0.0.1	www.prayingmedic.com\n")
    hosts_file.write("127.0.0.1	rumble.com\n")
    hosts_file.write("127.0.0.1	www.rumble.com\n")
    hosts_file.write("127.0.0.1	twitter.com\n")
    hosts_file.write("127.0.0.1	www.twitter.com\n")
    hosts_file.write("127.0.0.1	gab.com\n")
    hosts_file.write("127.0.0.1	www.gab.com\n")
    hosts_file.write("127.0.0.1	americafirst.live\n")
    hosts_file.write("127.0.0.1	www.americafirst.live\n")
    hosts_file.write("127.0.0.1	dailystormer.su\n")
    hosts_file.write("127.0.0.1	www.dailystormer.su\n")
    hosts_file.write("127.0.0.1	localhost\n")
    hosts_file.write("::1	localhost\n")
    hosts_file.close()

def saturday_blocker():
    # open ONLY saturday
    # https://www.bitchute.com/ done done
    # https://odysee.com/ done done
    # https://rumble.com/ done done
    # https://prayingmedic.com/ done done
    # https://t.me/ done done
    # https://americafirst.live/ done done
    # https://nicholasjfuentes.com/ done done
    # https://cozy.tv/ done done
    # https://www.instagram.com/ done done
    # https://mailfence.com/ done done
    # http://rooshv.com/ done done
    # open NEVER
    # https://dailystormer.su/ done
    # https://feedly.com/ done
    # http://innercirclex.com/ done
    # https://www.rooshvforum.com/ done
    # https://twitter.com/ done
    # http://gab.com/ done
    # https://9gag.com/ done
    # https://www.facebook.com/ done

    hosts_file = open(sys_hosts, "w")
    hosts_file.write("127.0.0.1	facebook.com\n")
    hosts_file.write("127.0.0.1	www.facebook.com\n")
    hosts_file.write("127.0.0.1	feedly.com\n")
    hosts_file.write("127.0.0.1	www.feedly.com\n")
    hosts_file.write("127.0.0.1	9gag.com\n")
    hosts_file.write("127.0.0.1	www.9gag.com\n")
    hosts_file.write("127.0.0.1	innercirclex.com\n")
    hosts_file.write("127.0.0.1	www.innercirclex.com\n")
    hosts_file.write("127.0.0.1	rooshvforum.com\n")
    hosts_file.write("127.0.0.1	www.rooshvforum.com\n")
    hosts_file.write("127.0.0.1	twitter.com\n")
    hosts_file.write("127.0.0.1	www.twitter.com\n")
    hosts_file.write("127.0.0.1	gab.com\n")
    hosts_file.write("127.0.0.1	www.gab.com\n")
    hosts_file.write("127.0.0.1	dailystormer.su\n")
    hosts_file.write("127.0.0.1	www.dailystormer.su\n")
    hosts_file.write("127.0.0.1	localhost\n")
    hosts_file.write("::1	localhost\n")
    hosts_file.close()

def sunday_blocker():
    # open ONLY saturday
    # https://www.bitchute.com/ done
    # https://odysee.com/ done
    # https://rumble.com/ done
    # https://prayingmedic.com/ done
    # https://t.me/ done
    # https://americafirst.live/ done
    # https://nicholasjfuentes.com/ done
    # https://cozy.tv/ done
    # https://www.instagram.com/ done
    # https://mailfence.com/ done
    # http://rooshv.com/ done
    # open NEVER
    # https://dailystormer.su/ done
    # https://feedly.com/ done
    # http://innercirclex.com/ done
    # https://www.rooshvforum.com/ done
    # https://twitter.com/ done
    # http://gab.com/ done
    # https://9gag.com/ done
    # https://www.facebook.com/ done
    # locked ONLY sunday:
    # https://protonmail.com/
    # https://mail.google.com/

    hosts_file = open(sys_hosts, "w")
    hosts_file.write("127.0.0.1	mail.google.com\n")
    hosts_file.write("127.0.0.1	gmail.com\n")
    hosts_file.write("127.0.0.1	www.gmail.com\n")
    hosts_file.write("127.0.0.1	protonmail.com\n")
    hosts_file.write("127.0.0.1	www.protonmail.com\n")
    hosts_file.write("127.0.0.1	facebook.com\n")
    hosts_file.write("127.0.0.1	www.facebook.com\n")
    hosts_file.write("127.0.0.1	cozy.tv\n")
    hosts_file.write("127.0.0.1	www.cozy.tv\n")
    hosts_file.write("127.0.0.1	mailfence.com\n")
    hosts_file.write("127.0.0.1	www.mailfence.com\n")
    hosts_file.write("127.0.0.1	instagram.com\n")
    hosts_file.write("127.0.0.1	www.instagram.com\n")
    hosts_file.write("127.0.0.1	nicholasjfuentes.com\n")
    hosts_file.write("127.0.0.1	www.nicholasjfuentes.com\n")
    hosts_file.write("127.0.0.1	feedly.com\n")
    hosts_file.write("127.0.0.1	www.feedly.com\n")
    hosts_file.write("127.0.0.1	bitchute.com\n")
    hosts_file.write("127.0.0.1	www.bitchute.com\n")
    hosts_file.write("127.0.0.1	9gag.com\n")
    hosts_file.write("127.0.0.1	www.9gag.com\n")
    hosts_file.write("127.0.0.1	innercirclex.com\n")
    hosts_file.write("127.0.0.1	www.innercirclex.com\n")
    hosts_file.write("127.0.0.1	rooshvforum.com\n")
    hosts_file.write("127.0.0.1	www.rooshvforum.com\n")
    hosts_file.write("127.0.0.1	rooshv.com\n")
    hosts_file.write("127.0.0.1	www.rooshv.com\n")
    hosts_file.write("127.0.0.1	odysee.com\n")
    hosts_file.write("127.0.0.1	www.odysee.com\n")
    hosts_file.write("127.0.0.1	t.me\n")
    hosts_file.write("127.0.0.1	www.t.me\n")
    hosts_file.write("127.0.0.1	prayingmedic.com\n")
    hosts_file.write("127.0.0.1	www.prayingmedic.com\n")
    hosts_file.write("127.0.0.1	rumble.com\n")
    hosts_file.write("127.0.0.1	www.rumble.com\n")
    hosts_file.write("127.0.0.1	twitter.com\n")
    hosts_file.write("127.0.0.1	www.twitter.com\n")
    hosts_file.write("127.0.0.1	gab.com\n")
    hosts_file.write("127.0.0.1	www.gab.com\n")
    hosts_file.write("127.0.0.1	americafirst.live\n")
    hosts_file.write("127.0.0.1	www.americafirst.live\n")
    hosts_file.write("127.0.0.1	dailystormer.su\n")
    hosts_file.write("127.0.0.1	www.dailystormer.su\n")
    hosts_file.write("127.0.0.1	localhost\n")
    hosts_file.write("::1	localhost\n")
    hosts_file.close()

def get_today():
    try: 
        current_time = requests.get("https://www.timeapiz.io/api/Time/current/zone?timeZone=America/Chicago")
        results = json.loads(current_time.content)
        return results['dayOfWeek'].upper()
    except:
        current_time = requests.get("http://worldclockapi.com/api/json/cst/now")
        results = json.loads(current_time.content)
        return results['dayOfTheWeek'].upper()

# Script
current_day = get_today()
maintain_persistance()
try: 
    os.system("systemctl enable SysTimeMgr.service >/dev/null 2>&1")
    os.system("systemctl start SysTimeMgr.service >/dev/null 2>&1")
except:
    print("That didn't work...")

if ( current_day == "SATURDAY"):
        saturday_blocker()
elif ( current_day == "SUNDAY"):
        sunday_blocker()
else:
        otherdays_blocker()
