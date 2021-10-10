#!/usr/bin/python3
# Library imports
# Version 1.04
import hashlib
import requests
import json

# Variables
sys_hosts = "/etc/hosts"
stop_weekday_procrastination_hash = "f7f1102f530c7b648a363d5897f3cf56"
stop_weekend_procrastination_hash = "5fd4717c654d578edb7809085b5b494a"
enable_procrastination_hash = "f845020ef7e7055e2cc0ee92e0ef9663"
saturday_blocker_hash = "6f828c11884499ab24e491e961e1c186"
sunday_blocker_hash = "2db95b5ebaf1492ef44ee9262c2192f"
otherdays_blocker_hash = "1b728acab5a719f3e0c985f66778f98b"



# Functions
def weekday_hosts():
    md5_sum = hashlib.md5(open(sys_hosts, 'rb').read()).hexdigest();

    if ( md5_sum == stop_weekend_procrastination_hash or md5_sum == stop_weekday_procrastination_hash):
        return True
    else:
        return False

def open_hosts():
    md5_sum = hashlib.md5(open(sys_hosts, 'rb').read()).hexdigest();

    if ( md5_sum == enable_procrastination_hash ):
        return True
    else:
        return False

def stop_weekday_procrastination():
    hosts_file = open(sys_hosts, "w")
    hosts_file.write("127.0.0.1	feedly.com\n")
    hosts_file.write("127.0.0.1	www.feedly.com\n")
    hosts_file.write("127.0.0.1	facebook.com\n")
    hosts_file.write("127.0.0.1	www.facebook.com\n")
    hosts_file.write("127.0.0.1	bitchute.com\n")
    hosts_file.write("127.0.0.1	www.bitchute.com\n")
    hosts_file.write("127.0.0.1	9gag.com\n")
    hosts_file.write("127.0.0.1	www.9gag.com\n")
    hosts_file.write("127.0.0.1	innercirclex.com\n")
    hosts_file.write("127.0.0.1	www.innercirclex.com\n")
    hosts_file.write("127.0.0.1	rooshvforum.com\n")
    hosts_file.write("127.0.0.1	www.rooshvforum.com\n")
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

def stop_weekend_procrastination():

    hosts_file = open(sys_hosts, "w")
    hosts_file.write("127.0.0.1	feedly.com\n")
    hosts_file.write("127.0.0.1	www.feedly.com\n")
    hosts_file.write("127.0.0.1	facebook.com\n")
    hosts_file.write("127.0.0.1	www.facebook.com\n")
    hosts_file.write("127.0.0.1	9gag.com\n")
    hosts_file.write("127.0.0.1	www.9gag.com\n")
    hosts_file.write("127.0.0.1	rooshvforum.com\n")
    hosts_file.write("127.0.0.1	www.rooshvforum.com\n")
    hosts_file.write("127.0.0.1	odysee.com\n")
    hosts_file.write("127.0.0.1	www.odysee.com\n")
    hosts_file.write("127.0.0.1	prayingmedic.com\n")
    hosts_file.write("127.0.0.1	www.prayingmedic.com\n")
    hosts_file.write("127.0.0.1	rumble.com\n")
    hosts_file.write("127.0.0.1	www.rumble.com\n")
    hosts_file.write("127.0.0.1	twitter.com\n")
    hosts_file.write("127.0.0.1	www.twitter.com\n")
    hosts_file.write("127.0.0.1	gab.com\n")
    hosts_file.write("127.0.0.1	www.gab.com\n")
    hosts_file.write("127.0.0.1	dailystormer.su\n")
    hosts_file.write("127.0.0.1	www.dailystormer.su\n")
    hosts_file.write("127.0.0.1	localhost\n")
    hosts_file.write("::1	localhost\n")
    hosts_file.close()

def saturday_blocker():
    # Everything but the following:
    # https://www.facebook.com/
    # https://feedly.com/
    # http://innercirclex.com/
    # https://www.rooshvforum.com/
    # https://twitter.com/
    # http://gab.com/
    # https://dailystormer.su/
    # https://9gag.com/


    hosts_file = open(sys_hosts, "w")
    hosts_file.write("127.0.0.1	facebook.com\n")
    hosts_file.write("127.0.0.1	www.facebook.com\n")
    hosts_file.write("127.0.0.1	feedly.com\n")
    hosts_file.write("127.0.0.1	www.feedly.com\n")
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
    hosts_file.write("127.0.0.1	9gag.com\n")
    hosts_file.write("127.0.0.1	www.9gag.com\n")
    hosts_file.write("127.0.0.1	localhost\n")
    hosts_file.write("::1	localhost\n")
    hosts_file.close()

def sunday_blocker():
    # protonmail.com, mailfence.com, mail.google.com


    hosts_file = open(sys_hosts, "w")
    hosts_file.write("127.0.0.1 protonmail.com")
    hosts_file.write("127.0.0.1 www.protonmail.com")
    hosts_file.write("127.0.0.1 mailfence.com")
    hosts_file.write("127.0.0.1 www.mailfence.com")
    hosts_file.write("127.0.0.1 mail.google.com")
    hosts_file.write("127.0.0.1 gmail.com")
    hosts_file.write("127.0.0.1 www.gmail.com")
    hosts_file.write("127.0.0.1	bitchute.com\n")
    hosts_file.write("127.0.0.1	www.bitchute.com\n")
    hosts_file.write("127.0.0.1	odysee.com\n")
    hosts_file.write("127.0.0.1	www.odysee.com\n")
    hosts_file.write("127.0.0.1	rumble.com\n")
    hosts_file.write("127.0.0.1	www.rumble.com\n")
    hosts_file.write("127.0.0.1	prayingmedic.com\n")
    hosts_file.write("127.0.0.1	www.prayingmedic.com\n")
    hosts_file.write("127.0.0.1	t.me\n")
    hosts_file.write("127.0.0.1	www.t.me\n")
    hosts_file.write("127.0.0.1	americafirst.live\n")
    hosts_file.write("127.0.0.1	www.americafirst.live\n")
    hosts_file.write("127.0.0.1 instagram.com\n")
    hosts_file.write("127.0.0.1 www.instagram.com\n")
    hosts_file.write("127.0.0.1	facebook.com\n")
    hosts_file.write("127.0.0.1	www.facebook.com\n")
    hosts_file.write("127.0.0.1	feedly.com\n")
    hosts_file.write("127.0.0.1	www.feedly.com\n")
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
    hosts_file.write("127.0.0.1	9gag.com\n")
    hosts_file.write("127.0.0.1	www.9gag.com\n")
    hosts_file.write("127.0.0.1	localhost\n")
    hosts_file.write("::1	localhost\n")
    hosts_file.close()

def otherdays_blocker():
    # https://www.bitchute.com/
    # https://odysee.com/
    # https://rumble.com/
    # https://prayingmedic.com/
    # https://t.me/
    # https://americafirst.live/
    # https://www.instagram.com/
    # --- Done already
    # https://www.facebook.com/
    # https://feedly.com/
    # http://innercirclex.com/
    # https://www.rooshvforum.com/
    # https://twitter.com/
    # http://gab.com/
    # https://dailystormer.su/
    # https://9gag.com/

    hosts_file = open(sys_hosts, "w")
    hosts_file.write("127.0.0.1	bitchute.com\n")
    hosts_file.write("127.0.0.1	www.bitchute.com\n")
    hosts_file.write("127.0.0.1	odysee.com\n")
    hosts_file.write("127.0.0.1	www.odysee.com\n")
    hosts_file.write("127.0.0.1	rumble.com\n")
    hosts_file.write("127.0.0.1	www.rumble.com\n")
    hosts_file.write("127.0.0.1	prayingmedic.com\n")
    hosts_file.write("127.0.0.1	www.prayingmedic.com\n")
    hosts_file.write("127.0.0.1	t.me\n")
    hosts_file.write("127.0.0.1	www.t.me\n")
    hosts_file.write("127.0.0.1	americafirst.live\n")
    hosts_file.write("127.0.0.1	www.americafirst.live\n")
    hosts_file.write("127.0.0.1 instagram.com\n")
    hosts_file.write("127.0.0.1 www.instagram.com\n")
    hosts_file.write("127.0.0.1	facebook.com\n")
    hosts_file.write("127.0.0.1	www.facebook.com\n")
    hosts_file.write("127.0.0.1	feedly.com\n")
    hosts_file.write("127.0.0.1	www.feedly.com\n")
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
    hosts_file.write("127.0.0.1	9gag.com\n")
    hosts_file.write("127.0.0.1	www.9gag.com\n")
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
md5_sum = hashlib.md5(open(sys_hosts, 'rb').read()).hexdigest();

if ( current_day == "SATURDAY"):
    if ( md5_sum != saturday_blocker_hash ):
        saturday_blocker()
elif ( current_day == "SUNDAY"):
    if ( md5_sum != sunday_blocker_hash ):
        sunday_blocker()
else:
    if ( md5_sum != otherdays_blocker_hash ):
        otherdays_blocker()