# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 14:25:54 2022

@author: kelly
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

kv = '''
BoxLayout:
    orientation: 'vertical'
    Button:
        text: app.pausePlay
        on_press: app.changePausePlay(self)
'''


class FirstKivy(App):
    pausePlay = StringProperty('Play')

    def __init__(self, **kwargs):
        super(FirstKivy, self).__init__(**kwargs)

    def build(self):
        layout = Builder.load_string(kv)
        return layout

    def changePausePlay(self, button):
        if self.pausePlay == "Play":
            self.pausePlay = "Pause"
        elif self.pausePlay == "Pause":
            self.pausePlay = "Play"

FirstKivy().run()
