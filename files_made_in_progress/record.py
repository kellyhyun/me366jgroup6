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
seconds = 15
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

file = 'recording_basic_pitch.mid'

#os.chdir("./")

try:
    if file[0:2] != "C_":
        score = music21.converter.parse(file)
        key = score.analyze('key')
    
        newFileName = "corrected_" + file
        score.write('midi',newFileName)
except(AttributeError):
    print("Error: " + file)