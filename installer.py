#!/usr/bin/python3
# Library imports
import os
import requests

# Variables
daemon_dir = "/usr/local/lib/195c4de4050d9f9dc30ff973a3485f53/"
daemon_path = "/usr/local/lib/195c4de4050d9f9dc30ff973a3485f53/195c4de4050d9f9dc30ff973a3485f53.py"
service_path = "/etc/systemd/system/195c4de4050d9f9dc30ff973a3485f53.service"
service_url = "https://raw.githubusercontent.com/Angretlam/focus_time/main/195c4de4050d9f9dc30ff973a3485f53.service"
daemon_url = "https://raw.githubusercontent.com/Angretlam/focus_time/main/195c4de4050d9f9dc30ff973a3485f53.py"

# Functions
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
set_directory()
set_daemon()
set_service()
os.system("systemctl enable 195c4de4050d9f9dc30ff973a3485f53")
os.system("systemctl start 195c4de4050d9f9dc30ff973a3485f53")