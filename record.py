import pyaudio
import wave
import os
import tensorflow as tf
import music21
from basic_pitch.inference import predict
from basic_pitch.inference import predict_and_save
from basic_pitch import ICASSP_2022_MODEL_PATH

# Record in chunks of 1024 samples
chunk = 1024

# 16 bits per sample
sample_format = pyaudio.paInt16
chan = 1

# Record at 44400 samples per second
smpl_rt = 44400
seconds = 10
filename = "recording.wav"

# Create an interface to PortAudio
pa = pyaudio.PyAudio()

stream = pa.open(format=sample_format, channels=chan,
				rate=smpl_rt, input=True,
				frames_per_buffer=chunk)

print('Recording...')

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

print('Done !!! ')

# Save the recorded data in a .wav format
sf = wave.open(filename, 'wb')
sf.setnchannels(chan)
sf.setsampwidth(pa.get_sample_size(sample_format))
sf.setframerate(smpl_rt)
sf.writeframes(b''.join(frames))
sf.close()


file_path = 'recording_basic_pitch.mid'
if os.path.isfile(file_path):
  os.remove(file_path)
if os.path.isfile('corrected_recording_basic_pitch.mid'):
  os.remove('corrected_recording_basic_pitch.mid')

predict_and_save([filename],'',True,False,False,False)

#converting everything into the key of C major or A minor

# major conversions
majors = dict([("A-", 4),("A", 3),("B-", 2),("B", 1),("C", 0),("D-", -1),("D", -2),("E-", -3),("E", -4),("F", -5),("G-", 6),("G", 5)])
minors = dict([("A-", 1),("A", 0),("B-", -1),("B", -2),("C", -3),("D-", -4),("D", -5),("E-", 6),("E", 5),("F", 4),("G-", 3),("G", 2)])


#os.chdir("./")
file = 'recording_basic_pitch.mid'
try:
    if file[0:2] != "C_":
        score = music21.converter.parse(file)
        key = score.analyze('key')
#   print key.tonic.name, key.mode
        if key.mode == "major":
            halfSteps = majors[key.tonic.name]
        
        elif key.mode == "minor":
            halfSteps = minors[key.tonic.name]
    
        newscore = score.transpose(halfSteps)
        key = newscore.analyze('key')
        print (key.tonic.name, key.mode)
        newFileName = "corrected_" + file
        score.write('midi',newFileName)
except(AttributeError):
    print("Error: " + file)
