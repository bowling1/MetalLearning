import pandas as pd
import numpy as np
from pytube import YouTube
from bs4 import BeautifulSoup
from requests import get
from time import time

MyData_file_path = 'C:\\Users\\aibow\\Python Projects\\MetalAnalyzer\\Metal Sheet 2 - Sheet1 - TEST.csv'
MyData = pd.read_csv(MyData_file_path)

#album_list = MyData["Album"]
#artist_list = MyData["Artist"]

#Inputs the artist and album name and outputs the youtube search link
def name_to_youtube_search(album, artist):
	album_splitname = album.split(" ")
	artist_splitname = artist.split(" ")
	youtube_search_url = "https://www.youtube.com/results?search_query="
	for i in range(len(album_splitname)):
		youtube_search_url += "+" + album_splitname[i]
	for i in range(len(artist_splitname)):
		youtube_search_url += "+" + artist_splitname[i]	
	return youtube_search_url

# inputs the youtube search link and outputs the link to the album video
def find_video_link(youtube_search, album_length):
	try:
		raw_html = get(youtube_search).text
	except:
		return "Invalid search query"
	search_html = BeautifulSoup(raw_html, "html.parser")
	linklist = search_html.find_all('a', class_= 'yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link')
	time_delta_top = 5
	for i in range(5):
		linklist[i] = "https://www.youtube.com" + linklist[i].attrs['href']
	for i in range(5):
		try:
			yt = YouTube(linklist[i])
		except:
			return "Invalid search query"
		time_delta_new = abs((int(yt.length)/60)-album_length)
		if time_delta_new<time_delta_top:
			time_delta_top = time_delta_new
			bestlink = linklist[i]
	if time_delta_top == 5:
		return "No video found"
	return bestlink

# Runs the other two functions as a 
def name_to_videolink(album, artist, length):
	youtube_search = name_to_youtube_search(album, artist)
	video_link = find_video_link(youtube_search, length)
	return video_link

link_list = []
for i in range(len(MyData["Album"])):
	#for i in range(3):
	i_albumlength = int(MyData.iloc[i,8])
	i_artist = str(MyData.iloc[i,2])
	i_album = str(MyData.iloc[i, 3])
	link_list.append(name_to_videolink(i_album, i_artist, i_albumlength))
	print(i)

link_series = pd.Series(link_list).astype(str)
MyData = pd.concat((MyData,link_series), axis=1)

MyData.to_csv("MusicSheet_Links", sep='\t', encoding='utf-8')