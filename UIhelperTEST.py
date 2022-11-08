# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 22:43:22 2022

@author: kelly
"""
import pandas as pd
import time

def readSong(filePath):
    return pd.read_csv(filePath, sep=',', header=0, low_memory = False)

def tester(filePath):
    time.sleep(1)
    song = readSong(filePath)
    for index, row in song.iterrows():
        note = row["Note"]
        delay = row["Delay"]
        note = note.split()
        print(note)
        time.sleep(delay)