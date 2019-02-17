# Chapter 02 - 03
import random

class Device:
    count = 0
    def __init__(self, ip, mac, name):
        self.ip = ip
        self.mac = mac
        self.name = name
        Device.count += 1
        # result: ping the device
        result = random.choice([False, True])
        self.status = 'active' if result else 'unknown'

class TV(Device):
    def turnon(self):
        # connect to self.ip and turn on
        print('turned on')
    
    def turnoff(self):
        # connect to self.ip and turn off
        print('turned off')

class Thermo(Device):
    def get_degree(self):
        # connect to self.ip and read the degree
        # return random number for demo
        return random.randint(0, 100)

tv1 = TV('120', 'ae-09', 'MyTV')
tv1.turnon()
print(tv1.status)

thermo = Thermo('121', 'ef-88', 'Thermo1')
print(thermo.get_degree())
print(thermo.status)
