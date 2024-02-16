import os
import subprocess
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def convert_mp4_to_wav(song_title):
    input_file = f'media/mp4/{song_title}.mp4'
    output_file = f'media/wav/{song_title}.wav'
    
    # Use the subprocess module to call the ffmpeg command
    command = [
        'ffmpeg',
        '-i', input_file,  # Input mp4 file
        '-ac', '2',        # Set the number of audio channels to 2 (stereo)
        '-ar', '44100',    # Set the audio sample rate to 44100 Hz
        '-vn',             # Disable video recording
        output_file        # Output wav file
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Conversion completed: {input_file} -> {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
