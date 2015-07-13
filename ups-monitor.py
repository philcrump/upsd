#!/usr/bin/python

serialPort = '/dev/ttyS0'
jsonPath = ''
csvPath = ''
pollTime = 30

from time import sleep
from os import system
from os.path import isfile
from Ups import Ups

ups = Ups(serialPort)
if not ups:
    print("Opening Serial Port failed!")
    exit()

if csvPath!='':
    if not isfile(csvPath):
        with open(csvPath, 'w') as outfile:
            outfile.write(ups.csvHeader())

while(1):
    while not ups.refresh():
        print("UPS Poll failed, sleeping..")
        sleep(5)
    
    print(ups.json())
    
    if jsonPath!='':
        with open(jsonPath, 'w') as outfile:
            outfile.write(ups.json())
    
    if csvPath!='':
        with open(csvPath, 'a') as outfile:
            outfile.write(ups.csv())
    
    if ups.batteryLow:
        if ups.refresh() and ups.batteryLow:
            system('/sbin/shutdown -h now &')
            
    sleep(pollTime)

