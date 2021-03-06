import os
import netmiko
from netmiko import ConnectHandler
from getpass import getpass
from datetime import date


login = input("Please enter your username: ")
pw = getpass("Please enter your password: ")
date = date.today().strftime("%m_%d_%Y")



router = {
        "ip" : "192.168.108.27", 
        "username" : login,
        "password" : pw,
        "device_type" : "cisco_ios"
}        
        
ch = ConnectHandler(**router)
        
        
conf = ch.send_command("show run")
        
f = open(f"ConfigSnap.config{date}" , "x")


f.write(conf)
f.close
