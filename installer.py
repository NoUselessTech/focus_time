#!/usr/bin/python3
# Library imports
import os
import requests

# Variables
script_dir = "/usr/local/bin/195c4de4050d9f9dc30ff973a3485f53/"
script_path = "/usr/local/bin/195c4de4050d9f9dc30ff973a3485f53/195c4de4050d9f9dc30ff973a3485f53.py"
daemon_dir = "/usr/local/lib/195c4de4050d9f9dc30ff973a3485f53/"
daemon_path = "/usr/local/lib/195c4de4050d9f9dc30ff973a3485f53/195c4de4050d9f9dc30ff973a3485f53.py"
service_path = "/etc/systemd/system/195c4de4050d9f9dc30ff973a3485f53.service"
service_url = "https://raw.githubusercontent.com/Angretlam/focus_time/main/195c4de4050d9f9dc30ff973a3485f53.service"
daemon_url = "https://raw.githubusercontent.com/Angretlam/focus_time/main/195c4de4050d9f9dc30ff973a3485f53.py"
script_url = "https://raw.githubusercontent.com/Angretlam/focus_time/main/focus_time.py"

# Functions
def set_script_directory():
    if os.path.isdir(script_dir) == False:
        os.mkdir(script_dir)
        print("Directory created")
    
    return True

def set_script():
    if os.path.isfile(script_path) == False:
        script_text = requests.get(script_url).text
        with open(script_path, "w") as service_file:
            service_file.write(script_text)

    print("Script created")
    return True
    return True

def set_cron():
    cron_file = open("/etc/crontab", "r")
    cron_lines = cron_file.readlines()
    cron_file.close()

    cron_exists = False
    expected_cron = "*/5 *	* * *   root    /usr/local/bin/195c4de4050d9f9dc30ff973a3485f53/195c4de4050d9f9dc30ff973a3485f53.py\n"

    for line in cron_lines:
        if line == expected_cron:
            cron_exists = True

    if cron_exists == False:
        cron_file = open("/etc/crontab", "a")
        cron_file.write(expected_cron)
        cron_file.close()

    return True

def set_directory():
    if os.path.isdir(daemon_dir) == False:
        os.mkdir(daemon_dir)
        print("Directory created")
    
    return True

def set_service():
    service_text = requests.get(service_url).text
    with open(service_path, "w") as service_file:
        service_file.write(service_text)

    print("Service created")
    return True

def set_daemon():
    daemon_text = requests.get(daemon_url).text
    with open(daemon_path, "w") as service_file:
        service_file.write(daemon_text)

    print("Daemon Saved")
    return True

# Logic
set_script_directory()
set_script()
set_cron()
set_directory()
set_daemon()
set_service()
os.system("systemctl enable 195c4de4050d9f9dc30ff973a3485f53")
os.system("systemctl start 195c4de4050d9f9dc30ff973a3485f53")
os.system("rm installer.py")

