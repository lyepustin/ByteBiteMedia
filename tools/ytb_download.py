import os
from pytube import YouTube
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def update_env_variable(variable_name, new_value):
    try:
        # Open the .env file in read mode
        with open(find_dotenv(), 'r') as file:
            lines = file.readlines()

        print(lines)

        # Find and update the specified variable
        for i, line in enumerate(lines):
            if line.startswith(f"{variable_name}="):
                lines[i] = f'{variable_name}="{new_value}"\n'
                break

        # Open the .env file in write mode and write the updated lines
        with open(find_dotenv(), 'w') as file:
            file.writelines(lines)

        print(f"{variable_name} updated successfully: {new_value}")
    except Exception as e:
        print(f"Error updating {variable_name}: {e}")


def download_audio(url, output_path='media'):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream
        audio_stream = yt.streams.get_audio_only()

        # Download the video to the specified output path
        audio_stream.download(output_path)

        print(f"{yt.title} downloaded successfully to {output_path}")
        
        update_env_variable("YOUTUBE_VIDEO_TITLE", yt.title)
    except Exception as e:
        print(f"Error: {e}")
