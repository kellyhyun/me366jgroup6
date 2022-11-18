from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import time
import pandas as pd
import serial 
import MidoAndRecord
from kivy.core.window import Window 


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
        # for each in note:
        #     sendData(each)
        time.sleep(delay)
        # sendData('p')
    # sendData('z')
        
def lightSong(filePath):
    song = readSong(filePath)
    time.sleep(3)
    for index, row in song.iterrows():
        note = row["Note"]
        delay = row["Delay"]
        note = note.split()
        print(note)
        # for each in note:
            # sendData(each)
        time.sleep(delay)
        # sendData('q')
    # sendData('z')

# def sendData(note):
#     if note == 'A':
#         arduino.write(str.encode('A'))
#     if note == 'B':
#         arduino.write(str.encode('B'))
#     if note == 'C':
#         arduino.write(str.encode('C'))
#     if note == 'D':
#         arduino.write(str.encode('D'))
#     if note == 'E':
#         arduino.write(str.encode('E'))
#     if note == 'F':
#         arduino.write(str.encode('F'))
#     if note == 'G':
#         arduino.write(str.encode('G'))
#     if note == '.G':
#         arduino.write(str.encode('H'))
#     if note == '.A':
#         arduino.write(str.encode('I'))
#     if note == '.B':
#         arduino.write(str.encode('J'))
#     if note == '^C':
#         arduino.write(str.encode('K'))
#     if note == '^D':
#         arduino.write(str.encode('L'))
#     if note == '^E':
#         arduino.write(str.encode('M'))
#     if note == '^F':
#         arduino.write(str.encode('N'))
#     if note == '^G':
#         arduino.write(str.encode('O'))
#     if note == 'p':
#         arduino.write(str.encode('p'))
#     if note == 'q':
#         arduino.write(str.encode('q'))
#     if note == 'z':
#         arduino.write(str.encode('z'))


class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    def play1(self):
        print("cantholdus")
        playSong('songs\C_cant_hold_us.csv')
    
    def play2(self):
        print("undersea")
        playSong('songs\C_Disney_Themes_-_Under_The_Sea.csv')

    def play3(self):
        print("newworld")
        playSong('songs\C_Disney_Themes_-_Whole_New_World.csv')

    def play4(self):
        print("stay")
        playSong('songs\C_rihanna_stay.csv')
        
    def play5(self):
        print("twinkle")
        playSong('songs\C_twinkle-twinkle-little-star.csv')


class ThirdWindow(Screen):
    def light1(self):
        print("cantholdus")
        lightSong('songs\C_cant_hold_us.csv')
    
    def light2(self):
        print("undersea")
        lightSong('songs\C_Disney_Themes_-_Under_The_Sea.csv')

    def light3(self):
        print("newworld")
        lightSong('songs\C_Disney_Themes_-_Whole_New_World.csv')

    def light4(self):
        print("stay")
        lightSong('songs\C_rihanna_stay.csv')
        
    def light5(self):
        print("twinkle")
        lightSong('songs\C_twinkle-twinkle-little-star.csv')

class FourthWindow(Screen):
    def record(self):
        print("recordingnow")
        MidoAndRecord.main()
    
    def playRecording(self):
        print("playrecording")
        playSong('corrected_recording_basic_pitch.csv')
  

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    reset()
    # portName = "COM6"
    # baudRate = 115200
    # arduino = serial.Serial(portName, baudRate)
    reset()
    MyMainApp().run()
    Window.close()
    
