# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 22:43:22 2022

@author: kelly
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 13:20:42 2022

@author: kelly
"""

import pandas as pd
import time
from userInterface1 import arduino


def readSong(filePath):
    return pd.read_csv(filePath, sep=',', header=0, low_memory = False)

def tester(filePath):
    song = readSong(filePath)
    time.sleep(3)
    for index, row in song.iterrows():
        note = row["Note"]
        delay = row["Delay"]
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

file = 'HotCrossBuns.csv'
tester(file)
arduino.close()

# import pandas as pd
# import time

# keepGoing = True

# def readSong(filePath):
#     return pd.read_csv(filePath, sep=',', header=0, low_memory = False)

# def tester(filePath, keepGoing):
#     keepGoing = True
#     time.sleep(1)
#     song = readSong(filePath)
#     for index, row in song.iterrows():
#         note = row["Note"]
#         delay = row["Delay"]
#         note = note.split()
#         print(note)
#         time.sleep(delay)