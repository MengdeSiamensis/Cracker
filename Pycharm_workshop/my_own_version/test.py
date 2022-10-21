import random

new_mac = ""
list = ['1','2','3','4','5','6','7','8','9','0']
x = lambda n: random.choice(n)+random.choice(n)+":"
for i in range(5):
    new_mac = new_mac + x(list)
print(random.choice(list))
print(new_mac)