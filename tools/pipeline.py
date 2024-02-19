from ytb_download import download_audio
from music_loop_detect import process_audio_data
from convert_utilities import convert_mp4_to_wav

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

video_url = os.getenv("YOUTUBE_URL_VIDEO")
song_title = download_audio(video_url, os.getenv("MEDIA_MP4_FOLDER"))
convert_mp4_to_wav(song_title)

win_lengths = [1]
min_lengths = [30, 60, 80]
process_audio_data(song_title, win_lengths, min_lengths)
