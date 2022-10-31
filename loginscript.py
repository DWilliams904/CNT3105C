import os
import netmiko
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import AuthenticationException
from netmiko.ssh_exception import SSHException
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

try:        
	ch = ConnectHandler(**router)
	conf = ch.send_command("show run")
	f = open(f"ConfigSnap.config{date}" , "x")
	f.write(conf)
	f.close
	
	
except (NetMikoTimeoutException):
	print("The following device has timed out: " + router["ip"])
except (AuthenticationException):
	print("Authentication failure on device: " + router["ip"])
except(SSHException):
	print("Could not connect to device via SSH. Please check SSH settings on: " + router["ip"])		
	
print("The script has completed")





