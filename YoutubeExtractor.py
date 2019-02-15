from __future__ import unicode_literals
import time
import youtube_dl
from subprocess import call

t1 = time.time()

Youtube_Link = "https://youtu.be/DxJxW67ftyE" # Moving forward, this should pull from another file that contains the list of links

# Options for the Youtube download
ydl_opts = {
    'format': 'worstaudio/worst', # Gives best audio quality possible. Say "worst" to get the opposite 
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav', # Chooses the file type output
        'preferredquality': '192' # Not 100% sure, but it reduced the size slightly when I set it to 50
    }],
    'postprocessor_args': [
        '-ar', '16000'
    ],
    'prefer_ffmpeg': True, # This is the default, don't change it if using ffmpeg isnetad of an alternative
    'keepvideo': False # If this is True, it produces a second, smaller file that's similar to a mp4
}

# The function that actually outputs the file. It saves to the same place the .py is located.
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([Youtube_Link])

t2 = time.time()
print(t2-t1) # Execution time for the entire code