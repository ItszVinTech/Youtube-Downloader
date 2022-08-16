print("Welcome to VJ YouTube Downloader and Converter v0.2 Alpha")
print("Loading...")

import time
import os
import streamlit as st

import pytube
import youtube_downloader
import file_converter

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# CODE
choice = st.sidebar.selectbox(
'How would you like to be contacted?',
('📺 Download Video', '📜 Download Playlist', '🎵 Download As MP3'))

print('''
What do you want?

(1) Download YouTube Videos Manually
(2) Download a YouTube Playlist
(3) Download YouTube Videos and Convert Into MP3

Downloading copyrighted YouTube videos is illegal!
I am not responsible for your downloads! Go at your own risk!

Copyright (c) VIJAY 2020
''')

#choice = st.text_input("Choice: ")

if choice == "📺 Download Video" or choice == "📜 Download Playlist":
    quality = st.sidebar.selectbox('Please Choose A Quality', 
    ('🏅 Low', '🥉 Medium', '🥈 High', '🥇 Very High')
    )
    
    if choice == "📜 Download Playlist":
        links = st.text_input("Enter the link to the playlist: ")
        print("Downloading playlist...")
        if quality == '🏅 Low':
            quality = 'low'
        elif quality == '🥉 Medium':
            quality = 'medium'
        elif quality == '🥈 High':
            quality = 'high'
        else:
            quality = 'very high'
        if st.button("Run"):
            youtube_downloader.download_playlist(links, quality)

            test = os.listdir("C://Users//kirth//OneDrive//Documents//Youtube//Python//Youtube-Web-Downloader")
            for item in test:
                if item.endswith(".mp4"):
                    video_file = open(item, 'rb')
                    video_bytes = video_file.read()
                    st.video(video_bytes)

            test = os.listdir("C://Users//kirth//OneDrive//Documents//Youtube//Python//Youtube-Web-Downloader")
            for item in test:
                if item.endswith(".mp4"):
                    time.sleep(30)
                    os.remove(os.path.join(dir_name, item))

    elif choice == "📺 Download Video":
        if quality == '🏅 Low':
            quality = 'low'
        elif quality == '🥉 Medium':
            quality = 'medium'
        elif quality == '🥈 High':
            quality = 'high'
        else:
            quality = 'very high'
        links = youtube_downloader.input_links()
        if st.button("Run"):
            filename = youtube_downloader.download_video(links, quality)
            video_file = open(filename, 'rb')
            video_bytes = video_file.read()
            st.video(video_bytes)
else:
    links = youtube_downloader.input_links()
    if links == "rickroll" or "rickastley" or "never gonna give u up" or "never gonna give you up" or "rick astley" or "easter egg" or "easteregg":
        links = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    print("Downloading...")
    if st.button("Run"):
        filename = youtube_downloader.download_video(links, 'low')
        print("Converting...")
        file_converter.convert_to_mp3(filename)
        if os.path.exists(filename):
            os.remove(filename)
        audio_file = open(filename[:-4] + ".wav", 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/wav')
        time.sleep(15)
        os.remove(filename[:-4] + ".wav")
