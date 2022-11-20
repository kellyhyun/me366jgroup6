from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import time
import pandas as pd
import serial 
import MidoAndRecord
from kivy.core.window import Window 
import threading
import pyaudio
import wave
import os
import tensorflow as tf
import music21
from basic_pitch.inference import predict
from basic_pitch.inference import predict_and_save
from basic_pitch import ICASSP_2022_MODEL_PATH
from kivy.clock import Clock
from kivy.properties import StringProperty


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
    global stopThread
    time.sleep(3)
    for index, row in song.iterrows():
        note = row["Note"]
        delay = row["Delay"]
        note = note.split()
        print(note)
        for each in note:
            sendData(each)
        time.sleep(delay)
        if stopThread == True:
            break
        sendData('p')
    sendData('z')
        
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
        if stopThread == True:
            break
        sendData('q')
    sendData('z')

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
    if note == 'z':
        arduino.write(str.encode('z'))

def setFilePlay(fileName):
    global action
    action = "play"
    global file
    file = fileName
    global returnScreen
    returnScreen = "play"
    global statusString
    statusString = "Playing {}".format(file)
    
def setFileLight(fileName):
    global action
    action = "light"
    global file
    file = fileName
    global returnScreen
    returnScreen = "light"
    global statusString
    statusString = "Playing {}".format(file)

def setFileRecord(fileName):
    global action
    action = "record"
    global file
    file = fileName
    global returnScreen
    returnScreen = "record"
    global statusString
    statusString = "Playing {}".format(file)



class MainWindow(Screen):
    pass

class SecondWindow(Screen):
        
    def play1(self):
        print("cantholdus")
        setFilePlay('songs\C_cant_hold_us.csv')
    
    def play2(self):
        print("undersea")
        setFilePlay('songs\C_Disney_Themes_-_Under_The_Sea.csv')
        
    def play3(self):
        print("newworld")
        setFilePlay('songs\C_Disney_Themes_-_Whole_New_World.csv')

    def play4(self):
        print("stay")
        setFilePlay('songs\C_rihanna_stay.csv')
        
    def play5(self):
        print("twinkle")
        setFilePlay('songs\C_twinkle-twinkle-little-star.csv')
    

class ThirdWindow(Screen):
    def light1(self):
        print("cantholdus")
        setFileLight('songs\C_cant_hold_us.csv')
    
    def light2(self):
        setFileLight('songs\C_Disney_Themes_-_Under_The_Sea.csv')

    def light3(self):
        print("newworld")
        setFileLight('songs\C_Disney_Themes_-_Whole_New_World.csv')

    def light4(self):
        print("stay")
        setFileLight('songs\C_rihanna_stay.csv')
        
    def light5(self):
        print("twinkle")
        setFileLight('songs\C_twinkle-twinkle-little-star.csv')

class FourthWindow(Screen):  
    recordString = StringProperty()
    recordString = "Waiting for instruction..."
        
    def start(self):
        print("recordingnow")
        # Record in chunks of 1024 samples
        global chunk
        chunk = 1024

        # 16 bits per sample
        global sample_format
        sample_format = pyaudio.paInt16
        global chan
        chan = 1

        # Record at 44400 samples per second
        global smpl_rt
        smpl_rt = 44400
        global seconds
        seconds = 15
        filename = "recording.wav"

        # Create an interface to PortAudio
        global pa
        pa = pyaudio.PyAudio()
        global stream
        stream = pa.open(format=sample_format, channels=chan,
        				rate=smpl_rt, input=True,
        				frames_per_buffer=chunk)

        print('Recording...')
        self.recordString = 'Recording...'
        self.ids.label2.text = self.recordString
        
        
    
    def middle(self):
        global chunk
        global sample_format
        global chan
        global smpl_rt
        global seconds
        global pa
        global stream
        
        filename = 'recording.wav'
        # Initialize array that be used for storing frames
        frames = []
        
        # Store data in chunks for 8 seconds
        for i in range(0, int(smpl_rt / chunk * seconds)):
        	data = stream.read(chunk)
        	frames.append(data)

        # Stop and close the stream
        stream.stop_stream()
        stream.close()

        # Terminate - PortAudio interface
        pa.terminate()

        # Save the recorded data in a .wav format
        sf = wave.open(filename, 'wb')
        sf.setnchannels(chan)
        sf.setsampwidth(pa.get_sample_size(sample_format))
        sf.setframerate(smpl_rt)
        sf.writeframes(b''.join(frames))
        sf.close()
        self.recordString = 'Done Recording. Create a CSV.'
        self.ids.label2.text = self.recordString
        print('Done !!! ')
        
    def almostEnd(self):
        self.recordString = 'Creating CSV File to Play Music.'
        self.ids.label2.text = self.recordString
        
        filename = 'recording.wav'

        file_path = 'recording_basic_pitch.mid'
        if os.path.isfile(file_path):
          os.remove(file_path)
        if os.path.isfile('corrected_recording_basic_pitch.mid'):
          os.remove('corrected_recording_basic_pitch.mid')

        predict_and_save([filename],'',True,False,False,False)

        file = 'recording_basic_pitch.mid'
        try:
            if file[0:2] != "C_":
                score = music21.converter.parse(file)
                key = score.analyze('key')
                newFileName = "corrected_" + file
                score.write('midi',newFileName)
        except(AttributeError):
            print("Error: " + file)
        
            
    def record(self):
        import mido
        import string
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
        def get_tempo(mid):
            for n in mid:     # Search for tempo
                if n.type == 'set_tempo':
                    return n.tempo
            return 500000       # If not found return default tempo
        midFile = 'corrected_recording_basic_pitch'
        if midFile == 'recording_basic_pitch' or 'corrected_recording_basic_pitch':
            lowLim = 90
            highLim = 93
        else:
            lowLim = 66
            highLim = 69
        mid = mido.MidiFile(midFile+'.mid', clip=True)
        # mid.tracks
        tempo = get_tempo(mid)
        bpm = (60000000/tempo)
        bps = bpm/60.0
        time = 0
        prevTime = 0
        mididict = []
        output = []
        # Put all note on/off in midinote as dictionary.
        for i in mid:
            if i.type == 'note_on' or i.type == 'note_off' or i.type == 'time_signature':
                mididict.append(i.dict())
            elif i.type == 'key_signature':
                key = i.dict()
                key = key['key']
        # change time values from delta to relative time.
        mem1=0
        # print(mididict)
        for i in mididict:
            time = i['time'] + mem1
            delay = time - prevTime
            i['time'] = time
            i['delay'] = delay
            mem1 = i['time']
        # make every note_on with 0 velocity note_off
            if i['type'] == 'note_on' and i['velocity'] == 0:
                i['type'] = 'note_off'
        # put note, starttime, stoptime, as nested list in a list. # format is [type, note, time, channel]
            mem2=[]
            if i['type'] == 'note_on': #or i['type'] == 'note_off':
                if i['note'] <= lowLim:
                    if i['note'] % 12 == 0:
                        i['note'] = 'C'
                    elif i['note'] % 12 == 1:
                        # i['note'] = 'C#'
                        i['note'] = ''
                    elif i['note'] % 12 == 2:
                        i['note'] = 'D'
                    elif i['note'] % 12 == 3:
                        # i['note'] = 'Eb'
                        i['note'] = ''
                    elif i['note'] % 12 == 4:
                        i['note'] = 'E'
                    elif i['note'] % 12 == 5:
                        i['note'] = 'F'
                    elif i['note'] % 12 == 6:
                        # i['note'] = 'F#'
                        i['note'] = ''
                    elif i['note'] % 12 == 7:
                        i['note'] = '.G'
                    elif i['note'] % 12 == 8:
                        # i['note'] = '.G#'
                        i['note'] = ''
                    elif i['note'] % 12 == 9:
                        i['note'] = '.A'
                    elif i['note'] % 12 == 10:
                        # i['note'] = '.Bb'
                        i['note'] = ''
                    elif i['note'] % 12 == 11:
                        i['note'] = '.B'
                elif i['note'] >= highLim:
                    if i['note'] % 12 == 0:
                        i['note'] = '^C'
                    elif i['note'] % 12 == 1:
                        # i['note'] = '^C#'
                        i['note'] = ''
                    elif i['note'] % 12 == 2:
                        i['note'] = '^D'
                    elif i['note'] % 12 == 3:
                        # i['note'] = '^Eb'
                        i['note'] = ''
                    elif i['note'] % 12 == 4:
                        i['note'] = '^E'
                    elif i['note'] % 12 == 5:
                        i['note'] = '^F'
                    elif i['note'] % 12 == 6:
                        # i['note'] = '^F#'
                        i['note'] = ''
                    elif i['note'] % 12 == 7:
                        i['note'] = '^G'
                    elif i['note'] % 12 == 8:
                        # i['note'] = '^G#'
                        i['note'] = ''
                    elif i['note'] % 12 == 9:
                        i['note'] = 'A'
                    elif i['note'] % 12 == 10:
                        # i['note'] = 'Bb'
                        i['note'] = ''
                    elif i['note'] % 12 == 11:
                        i['note'] = 'B'
                else:
                    if i['note'] % 12 == 7:
                        i['note'] = 'G'
                    elif i['note'] % 12 == 8:
                        # i['note'] = 'G#'
                        i['note'] = ''

                # mem2.append(i['type'])
                mem2.append(i['note'])
                mem2.append(i['time'])
                mem2.append(np.round(i['delay']*bps*16)/(bps*16))
                mem2.append(i['channel'])
                # if mem2[3] == 4:
                output.append(mem2)
                prevTime = i['time']
                
        # put timesignatures
            elif i['type'] == 'time_signature':

                mem2 = []
                mem2.append('Note')
                mem2.append('Time')
                mem2.append("Delay")
                mem2.append('Channel')
                output.append(mem2)

                prevTime = i['time']
        # viewing the midimessages.

        for n in range(1,len(output)):
            # if str(output[n][2]).isnumeric():
            try:
                output[n][2] = output[n+1][2]
            except IndexError:
                output[n][2] = 0.0
            # print(output[n][2])

        m = 1
        while m < len(output):
            try:
                if (output[m][0][-1] == output[m-1][0][-1] or output[m][0][0] == output[m-1][0][0]) and (output[m-1][2] == 0):# and (output[m-1][3] == output[m][3]):
                    output[m][0] = output[m-1][0]
                    del output[m-1]
                elif (output[m-1][2] == 0.0):# and (output[m-1][3] == output[m][3]):
                    output[m][0] = output[m-1][0] + " " + output[m][0]
                    del output[m-1]
                else:
                    m+=1
            except (IndexError):
                if output[m][0] == '' and (output[m-1][2] == 0):# and (output[m-1][3] == output[m][3]):
                    output[m][0] = output[m-1][0]
                    del output[m-1]
                elif output[m][0] == '':
                    del output[m]
                elif (output[m-1][2] == 0):# and (output[m-1][3] == output[m][3]):
                    output[m][0] = output[m-1][0] + " " + output[m][0]
                    del output[m-1]
                else:
                    m+=1
        for line in output:
            for n in range(len(line[0])):
                for nn in range(n+1, len(line[0])):
                    try:
                        if line[0][n] == ' ' or line[0][n] == '.' or line[0][n] == '^':
                            continue
                        elif line[0][n] == line[0][nn]:
                            if line[0][nn-1] == '.' or line[0][nn-1] == '^':
                                line[0] = line[0][:nn-1] + line[0][nn:]
                                nn-=1
                            try:
                                line[0] = line[0][:nn] + line[0][nn+2:]
                            except(IndexError):
                                line[0] = line[0][:nn]
                    except(IndexError):
                        continue
                        
                        

        for i in output:
            print(i)
        # print(mid)
        print(mid.ticks_per_beat)
        arr = np.asarray(output)

        pd.DataFrame(arr).to_csv(midFile+'.csv', header=False)
        
        self.recordString = "Finished CSV File - Ready to Play"
        self.ids.label2.text = self.recordString
    
    def playRecording(self):
        print("playrecording")
        setFileRecord('corrected_recording_basic_pitch.csv')
  
    
class FifthWindow(Screen):
    
    def returnBack(self):
        self.ids.label1.text = "Waiting for Instruction"
        global stopThread
        stopThread = True
        global returnScreen
        print(returnScreen)
        return returnScreen
        
    
    def startSong(self):
        print('startThread')
        global action
        global file
        global thread
        if (action == "play"):
            thread = threading.Thread(target=playSong, args=(file,))
        if (action == "light"):
            thread = threading.Thread(target=lightSong, args=(file,))
        if (action == "record"):
            thread = threading.Thread(target=playSong, args=(file,))
        global stopThread
        stopThread = False
        thread.start()
        global statusString
        self.ids.label1.text = statusString
        
    def stopSong(self):
        print("stopThread")
        global stopThread
        stopThread = True
        self.ids.label1.text = "Stopped Song - Waiting for Instruction"

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("stop.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    reset()
    portName = "COM3"
    baudRate = 115200
    arduino = serial.Serial(portName, baudRate)
    reset()
    MyMainApp().run()
    Window.close()
    
