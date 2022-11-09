# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 13:20:42 2022

@author: kelly
"""

import pandas as pd
import time
import serial

file = 'C_Disney_Themes_-_Whole_New_World.csv'

portName = "COM4"
baudRate = 115200
arduino = serial.Serial(portName, baudRate)

def readSong(filePath):
    return pd.read_csv(filePath, sep=',', header=0, low_memory = False)

def playSong(filePath):
    
    song = readSong(filePath)
    print(song)
    time.sleep(5)
    for index, row in song.iterrows():
        note = row["Note"]
        delay = row["Delay"]
        print(note, delay)
        note = note.split()
        for each in note:
            # time.sleep(0.005)
            sendData(each)
        time.sleep(delay)
        sendData('p')
        

def sendData(note):
    if note == 'A':
        arduino.write(str.encode('A'))
    if note == 'B':
        arduino.write(str.encode('B'))
    if note == 'C':
        arduino.write(str.encode('C'))
    #    print("I Work")
    if note == 'D':
        arduino.write(str.encode('D'))
    if note == 'E':
        arduino.write(str.encode('E'))
    if note == 'F':
        arduino.write(str.encode('F'))
    if note == 'G':
        arduino.write(str.encode('G'))
    if note == '.G':
        arduino.write(str.encode('H'))
    if note == '.A':
        arduino.write(str.encode('I'))
    if note == '.B':
        arduino.write(str.encode('J'))
    if note == '^C':
        arduino.write(str.encode('K'))
    if note == '^D':
        arduino.write(str.encode('L'))
    if note == '^E':
        arduino.write(str.encode('M'))
    if note == '^F':
        arduino.write(str.encode('N'))
    if note == '^G':
        arduino.write(str.encode('O'))
    if note == 'p':
        arduino.write(str.encode('p'))

playSong(file)
sendData('A')
sendData('B')
# sendData('p')
arduino.close()