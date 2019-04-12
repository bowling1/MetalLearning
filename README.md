# Metal Learning



IDEAS
- Scrape Youtube links from last.fm (names of albums from spreadsheet), then put them in the dataframe to compare with the genre.
- Or.... scrape links directly from youtube, since searching has the namekeys directly in the url.


NOTES
- Get spectrogram of section (https://librosa.github.io/librosa/generated/librosa.display.specshow.html), no x-axis/y-axis, force grayscale. Then convert to 2d numpy array (https://stackoverflow.com/questions/40727793/how-to-convert-a-grayscale-image-into-a-list-of-pixel-values) to put through Keras.
- Good outline of plan (https://hackernoon.com/finding-the-genre-of-a-song-with-deep-learning-da8f59a61194)


CURRENT PLAN
Create an an app that after a few seconds of listening to a song, it says the genre of metal it is. Problems would be the actual accessability, since you'd be recording from a phone, and outputting through (non-ideally) live music or something else that has a muddy sound. It'd HAVE to be recorded music being output at an optimal distance from the phone, or I'd have to do tons of pre-processing before the input even gets to the model. Maybe better to have it be a whole song, but that may be very slow and defeats the purpose of there being an app.
