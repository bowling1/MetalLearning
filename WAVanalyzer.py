from __future__ import print_function
import librosa
import pydub
import glob, sys, os

def mp3_to_wav(file):
	sound = pydub.AudioSegment.from_mp3(file)
	sound.export("C:\\Users\\aibow\\Python Projects\\MP3\\Dark Funeral - My Funeral.wav", format="wav")

# 1. Get the file path to the included audio example
filename_mp3 = "C:\\Users\\aibow\\Python Projects\\MP3\\Dark Funeral - My Funeral.mp3"

file_wav = mp3()
print("File changed to .wav")

# 2. Load the audio as a waveform `y`
#    Store the sampling rate as `sr`
y, sr = librosa.load(file_wav)

# 3. Run the default beat tracker
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

# 4. Convert the frame indices of beat events into timestamps
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

print(beat_times)
print(type(beat_times))
