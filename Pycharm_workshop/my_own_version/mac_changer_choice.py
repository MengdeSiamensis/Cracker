#!/usr/bin/env python
import subprocess
import random
import time
import math

def change_mac(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    subprocess.call(["ifconfig"])

def random_MAC_address(time_loop_minute):
    time_loop_convert = math.floor(time_loop_minute * 60)
    num1 = ['1','2','3','4','5','6','7','8','9'] #00:11:22:33:44:55
    num2 = ['A','B','C','D','E','F','1','2','3','4','5','6','7','8','9']
    new_mac = "00:"+str(random.choice(num1))+str(random.choice(num2))+":"+str(random.choice(num1))+str(random.choice(num2))+":"+str(random.choice(num1))+str(random.choice(num2))+":"+str(random.choice(num1))+str(random.choice(num2))+":"+str(random.choice(num1))+str(random.choice(num2))
    print(new_mac)
    change_mac(interface, new_mac)
    time.sleep(time_loop_convert)

print("You have 2 choices \n\t1.auto mode its will change your MAC_address automatically by random type <auto> \n\t2.manual mode change your MAC_address by yourself <man>")
print("Enter your interface : ")
interface = input()
print('Enter your choice : ')
choice = input()

if choice == "auto":
    print("You have 2 choices \n\t1.enternity will change your mac address forever type <ent> \n\t2.count mode this will change mac address in the time you take an input loop <count>")
    print("make your decision : ")
    decision = input()
    print("please choose your time loop in minute : ")
    time_loop_minute = input()
    if decision == "ent":
        while True:
            random_MAC_address(float(time_loop_minute))
    elif decision == "count":
        print("How many time you want to loop : ")
        time_spam = input()
        i = 0
        while i < int(time_spam):
            random_MAC_address(float(time_loop_minute))
            i += 1
            print(i)
elif choice == "man":
    print("please enter your new_mac : ")
    input_new_mac = input()
    change_mac(interface,input_new_mac)



