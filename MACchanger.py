import subprocess

try:
    interface_name = input("Enter your interface name: ")
    mac_address = input("Enter MAC address: ")
except KeyboardInterrupt:
    print("\nexit")
    exit()
except Exception:
    print("\nexit")
    exit()
subprocess.run("ifconfig " + interface_name + " down", shell= True)
subprocess.run("ifconfig " + interface_name + " hw ether " + mac_address, shell=True)
subprocess.run("ifconfig " + interface_name + " up", shell=True)

print("mac address changed succesfully")
