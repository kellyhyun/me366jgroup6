#%%

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


midFile = 'recording_basic_pitch'
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
        if i['note'] <= 66:
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
        elif i['note'] >= 69:
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
        # mem2.append(i['type'])
        # mem2.append(i['numerator'])
        # mem2.append(i['denominator'])
        # mem2.append(i['time'])
        # # mem2.append(int(i['delay']*bps))
        # output.append(mem2)

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
print(mid.ticks_per_beat)
# print(mid.tracks)
# print(key)

arr = np.asarray(output)

pd.DataFrame(arr).to_csv(midFile+'.csv', header=False)

# below are functions to find all the info you'd ever need out of Midi files

# def msg2dict(msg):
#     result = dict()
#     if 'note_on' in msg:
#         on_ = True
#     elif 'note_off' in msg:
#         on_ = False
#     else:
#         on_ = None
#     result['time'] = int(msg[msg.rfind('time'):].split(' ')[0].split('=')[1].translate(
#         str.maketrans({a: None for a in string.punctuation})))

#     if on_ is not None:
#         for k in ['note', 'velocity']:
#             result[k] = int(msg[msg.rfind(k):].split(' ')[0].split('=')[1].translate(
#                 str.maketrans({a: None for a in string.punctuation})))
#     return [result, on_]

# def switch_note(last_state, note, velocity, on_=True):
#     # piano has 88 notes, corresponding to note id 21 to 108, any note out of this range will be ignored
#     result = [0] * 88 if last_state is None else last_state.copy()
#     if 21 <= note <= 108:
#         result[note-21] = velocity if on_ else 0
#     return result


# def get_new_state(new_msg, last_state):
#     new_msg, on_ = msg2dict(str(new_msg))
#     new_state = switch_note(last_state, note=new_msg['note'], velocity=new_msg['velocity'], on_=on_) if on_ is not None else last_state
#     return [new_state, new_msg['time']]

# def track2seq(track):
#     # piano has 88 notes, corresponding to note id 21 to 108, any note out of the id range will be ignored
#     result = []
#     last_state, last_time = get_new_state(str(track[0]), [0]*88)
#     for i in range(1, len(track)):
#         new_state, new_time = get_new_state(track[i], last_state)
#         if new_time > 0:
#             result += [last_state]*new_time
#         last_state, last_time = new_state, new_time
#     return result

# def mid2arry(mid, min_msg_pct=0.1):
#     tracks_len = [len(tr) for tr in mid.tracks]
#     min_n_msg = max(tracks_len) * min_msg_pct
#     # convert each track to nested list
#     all_arys = []
#     for i in range(len(mid.tracks)):
#         if len(mid.tracks[i]) > min_n_msg:
#             ary_i = track2seq(mid.tracks[i])
#             all_arys.append(ary_i)
#     # make all nested list the same length
#     max_len = max([len(ary) for ary in all_arys])
#     for i in range(len(all_arys)):
#         if len(all_arys[i]) < max_len:
#             all_arys[i] += [[0] * 88] * (max_len - len(all_arys[i]))
#     all_arys = np.array(all_arys)
#     all_arys = all_arys.max(axis=0)
#     # trim: remove consecutive 0s in the beginning and at the end
#     sums = all_arys.sum(axis=1)
#     ends = np.where(sums > 0)[0]
#     return all_arys[min(ends): max(ends)]

# def arry2mid(ary, tempo=500000):
#     # get the difference
#     new_ary = np.concatenate([np.array([[0] * 88]), np.array(ary)], axis=0)
#     changes = new_ary[1:] - new_ary[:-1]
#     # create a midi file with an empty track
#     mid_new = mido.MidiFile()
#     track = mido.MidiTrack()
#     mid_new.tracks.append(track)
#     track.append(mido.MetaMessage('set_tempo', tempo=tempo, time=0))
#     # add difference in the empty track
#     last_time = 0
#     for ch in changes:
#         if set(ch) == {0}:  # no change
#             last_time += 1
#         else:
#             on_notes = np.where(ch > 0)[0]
#             on_notes_vol = ch[on_notes]
#             off_notes = np.where(ch < 0)[0]
#             first_ = True
#             for n, v in zip(on_notes, on_notes_vol):
#                 new_time = last_time if first_ else 0
#                 track.append(mido.Message('note_on', note=n + 21, velocity=v, time=new_time))
#                 first_ = False
#             for n in off_notes:
#                 new_time = last_time if first_ else 0
#                 track.append(mido.Message('note_off', note=n + 21, velocity=0, time=new_time))
#                 first_ = False
#             last_time = 0
#     return mid_new

    
# result_array = mid2arry(mid)
# plt.plot(range(result_array.shape[0]), np.multiply(np.where(result_array>0, 1, 0), range(1, 89)), marker='.', markersize=1, linestyle='')
# plt.title("twinkle-twinkle-little-star.mid")
# plt.show()

# print(result_array)