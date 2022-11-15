# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 23:17:35 2022

@author: kelly
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window 
import time
import pandas as pd
import serial 
import MidoAndRecord

def readSong(filePath):
    return pd.read_csv(filePath, sep=',', header=0, low_memory = False)

def reset():
    import kivy.core.window as window
    from kivy.base import EventLoop
    if not EventLoop.event_listeners:
        from kivy.cache import Cache
        window.Window = window.core_select_lib('window', window.window_impl, True)
        Cache.print_usage()
        for cat in Cache._categories:
            Cache._objects[cat] = {}
            
def playSong(filePath):
    song = readSong(filePath)
    time.sleep(3)
    for index, row in song.iterrows():
        note = row["Note"]
        delay = row["Delay"]
        note = note.split()
        print(note)
        for each in note:
            sendData(each)
        time.sleep(delay)
        sendData('p')
        
def lightSong(filePath):
    song = readSong(filePath)
    time.sleep(3)
    for index, row in song.iterrows():
        note = row["Note"]
        delay = row["Delay"]
        note = note.split()
        print(note)
        for each in note:
            sendData(each)
        time.sleep(delay)
        sendData('q')

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
    if note == 'q':
        arduino.write(str.encode('q'))

class RootWidget(BoxLayout):
    def __init__(self, **kwargs): 
        super(RootWidget, self).__init__(**kwargs)

    def play1(self):
        print("Twinkle")
        playSong('TwinkleTwinkleSimple.csv')
    
    def play2(self):
        print("HotCrossBuns")
        playSong('HotCrossBuns.csv')

    def light1(self):
        print("Twinkle")
        lightSong('TwinkleTwinkleSimple.csv')
    
    def light2(self):
        print("HotCrossBuns")
        lightSong('HotCrossBuns.csv')
    
    def record(self):
        MidoAndRecord.main()
    
    def play2(self):
        print("RecordingPlay")
        playSong('recording_basic_pitch.csv')

class TestApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    reset()
    portName = "COM6"
    baudRate = 115200
    arduino = serial.Serial(portName, baudRate)
    reset()
    TestApp().run()
    Window.close()