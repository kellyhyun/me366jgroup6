# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 13:20:42 2022

@author: kelly
"""

import pandas as pd
import time
import serial

file = 'MidiTest.csv' #can use just the file name, not the full path, if it is in the same folder. This will make it easier to transfer code between computers

portName = "COM3"
baudRate = 115200
arduino = serial.Serial(portName, baudRate)

def readSong(filePath):
    return pd.read_csv(filePath, sep=',', header=0, low_memory = False)

def playSong(filePath):
    time.sleep(5)
    song = readSong(filePath)
    for index, row in song.iterrows():
        note = row["Note"]
        delay = row["Delay"]
        note = note.split()
        for each in note:
            sendData(each)
        time.sleep(delay)
        sendData('p')
        
# TEST FUNCTION FOR UI
def tester(filePath):
    time.sleep(5)
    song = readSong(filePath)
    for index, row in song.iterrows():
        note = row["note"]
        delay = row["delay"]
        note = note.split()
        for each in note:
            print(each)
        time.sleep(delay)
        

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
arduino.close()