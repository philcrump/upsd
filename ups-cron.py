#!/usr/bin/python2

serialPort = '/dev/ttyS0'
jsonPath = ''
csvPath = ''

from time import sleep
from os import system
from os.path import isfile
from Ups import Ups

ups = Ups(serialPort)
if not ups:
    print("Opening Serial Port failed!")
    exit()

if not ups.refresh():
    print("Refreshing UPS Values failed!")
    exit()

if csvPath!='':
    if not isfile(csvPath):
        with open(csvPath, 'w') as outfile:
            outfile.write(ups.csvHeader())

if jsonPath!='':
    with open(jsonPath, 'w') as outfile:
        outfile.write(ups.json())

if csvPath!='':
    with open(csvPath, 'a') as outfile:
        outfile.write(ups.csv())

if ups.batteryLow:
    if ups.refresh() and ups.batteryLow:
        system('/sbin/shutdown -h now "### UPS Power Failure ###"&')

