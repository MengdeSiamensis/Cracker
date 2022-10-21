#!/usr/bin/env python


import scapy.all as scapy
import optparse

def ip_request():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="IP_address", help="Add IP")
    (option, arguments) = parser.parse_args()
    return option


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    boardcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_boardcast = boardcast/arp_request
    answered_list = scapy.srp(arp_request_boardcast, timeout=1, verbose=False)[0]

    
    clients_list = []
    for element in answered_list:
        client_dict = {"ip" :element[1].psrc, "mac":element[1].hwsrc}
        clients_list.append(client_dict)
        #print(element[1].psrc + "\t\t" + element[1].hwsrc)
    return clients_list

def print_result(result_list):
    print("IP\t\t\tMAC Address\n-------------------------------")
    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])



#int main
option = ip_request()


print_result(scan(option.IP_address))
print("\nWell done!")