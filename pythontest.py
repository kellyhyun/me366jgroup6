# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 13:20:42 2022

@author: kelly
"""

import pandas as pd
import time
import serial

file = r'C:/Users/kelly/OneDrive/Documents/homework/!Fall 2023/ME366J/Song1.csv'

portName = "COM3"
baudRate = 115200
arduino = serial.Serial(portName, baudRate)

def readSong(filePath):
    return pd.read_csv(filePath, sep=',', header=0, low_memory = False)

def playSong(filePath):
    time.sleep(5)
    song = readSong(filePath)
    for index, row in song.iterrows():
        note = row["note"]
        delay = row["delay"]
        note = note.split()
        for each in note:
            sendData(each)
        time.sleep(delay)
        sendData('p')
        
'''
if there is zero delay for notes played at the same time
def playSong(filePath):
    time.sleep(5)
    song = readSong(filePath)
    for index, row in song.iterrows():
        note = row["note"]
        delay = row["delay"]
        sendData(note)
        time.sleep(delay)
'''
        

def sendData(note):
    if note == 'A':
        arduino.write(str.encode('A'))
    if note == 'B':
        arduino.write(str.encode('B'))
    if note == 'p':
        arduino.write(str.encode('play'))

playSong(file)
sendData('A')
sendData('B')