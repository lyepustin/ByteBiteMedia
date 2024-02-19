import subprocess
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


def get_audio_info(audio_file_path):
    command = [
        'ffprobe',
        '-v', 'error',
        '-show_format',
        '-show_streams',
        '-of', 'json',
        audio_file_path
    ]

    output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return output.stdout.strip()


song_title = os.getenv("YOUTUBE_VIDEO_TITLE")
audio_file_path = f'media/wav/{song_title}.wav'
output = get_audio_info(audio_file_path)
print(output)