import subprocess

interface_name = input("Enter your interface name: ")
mac_address = input("Enter MAC address name: ")

subprocess.run("ifconfig " + interface_name + " down", shell = True)
subprocess.run("ifconfig " + interface_name + " hw ether " + mac_address, shell = True)
subprocess.run("ifconfig " + interface_name + " up", shell = True)

print("MAC-address changed succesfully")