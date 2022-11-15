import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button # You would need futhermore this
from kivy.uix.boxlayout import BoxLayout
# import pythontest as pt
import serial 
import pandas as pd
import time

# Notes that we have for milestone - C E F G A 
def readSong(filePath):
    return pd.read_csv(filePath, sep=',', header=0, low_memory = False)

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

# #TESTING WITHOUT ARDUINO
# def tester(filePath):
#     time.sleep(1)
#     song = readSong(filePath)
#     for index, row in song.iterrows():
#         note = row["Note"]
#         delay = row["Delay"]
#         note = note.split()
#         print(note)
#         time.sleep(delay)
        
def reset():
    import kivy.core.window as window
    from kivy.base import EventLoop
    if not EventLoop.event_listeners:
        from kivy.cache import Cache
        window.Window = window.core_select_lib('window', window.window_impl, True)
        Cache.print_usage()
        for cat in Cache._categories:
            Cache._objects[cat] = {}

class ButtonApp(App):
     
    def build(self):
        layout = BoxLayout()

        # use a (r, g, b, a) tuple
        btn1 = Button(text = "Twinkle Twinkle Little Star",
                   font_size ="15sp",
                   background_color =(1, 1, 1, 1),
                   color =(1, 1, 1, 1),
                   size =(32, 32),
                   size_hint =(.2, .2),
                   pos =(150, 250))
 
        # bind() use to bind the button to function callback
        btn1.bind(on_press = self.callback)
        
        btn2 = Button(text ="Hot Cross Buns",
                   font_size ="15sp",
                   background_color =(1, 1, 1, 1),
                   color =(1, 1, 1, 1),
                   size =(32, 32),
                   size_hint =(.2, .2),
                   pos =(300, 250))
 
        # bind() use to bind the button to function callback
        btn2.bind(on_press = self.callback2)
        
        exitB = Button(text ="exit",
                   font_size ="20sp",
                   background_color =(1, 1, 1, 1),
                   color =(1, 1, 1, 1),
                   size =(16, 16),
                   size_hint =(.2, .2),
                   pos =(300, 0))
        exitB.bind(on_press = self.close_application)
        
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(exitB)
        
        return layout
 
    # callback function tells when button pressed
    def callback(self, event):
        print("Twinkle")
        playSong('TwinkleTwinkleSimple.csv')
        
    def callback2(self, event):
        print("HotCrossBuns")
        playSong('HotCrossBuns.csv')
        
    def close_application(self, event):
        # closing application
        App.get_running_app().stop()
        # removing window
        Window.close()
 
# creating the object root for ButtonApp() class
root = ButtonApp()

if __name__ == '__main__':
    reset()
    portName = "COM6"
    baudRate = 115200
    arduino = serial.Serial(portName, baudRate)
    root.run()
    Window.close()
    arduino.close()
    
