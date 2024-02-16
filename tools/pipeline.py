from ytb_download import download_audio
from music_loop_detect import process_audio_data
from convert_utilities import convert_mp4_to_wav

import os
from dotenv import load_dotenv, find_dotenv


video_url = "https://youtu.be/6At10g4UlmE"
download_audio(video_url, os.getenv("MEDIA_MP4_FOLDER"))
load_dotenv(find_dotenv())

song_title = os.getenv("YOUTUBE_VIDEO_TITLE")
print(song_title)
convert_mp4_to_wav(song_title)

win_lengths = [1, 5, 10, 15, 20, 30, 40, 60]
min_lengths = [1]
process_audio_data(song_title, win_lengths, min_lengths)
