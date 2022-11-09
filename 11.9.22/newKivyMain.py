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
def tester(filePath):
    time.sleep(1)
    song = readSong(filePath)
    for index, row in song.iterrows():
        note = row["Note"]
        delay = row["Delay"]
        note = note.split()
        print(note)
        time.sleep(delay)

class RootWidget(BoxLayout):
    def __init__(self, **kwargs): 
        super(RootWidget, self).__init__(**kwargs)

    def callback(self):
        print("Twinkle")
        tester('TwinkleTwinkleSimple.csv')
    
    def callback2(self):
        print("HotCrossBuns")
        tester('HotCrossBuns.csv')



class TestApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    reset()
    TestApp().run()
    Window.close()