import os
import numpy as np
import soundfile as sf
import librosa
from dotenv import load_dotenv, find_dotenv
from librosa_loopfinder import find_loop_points


def process_audio_data(song_title, win_lengths, min_lengths):
    song_file = f'media/wav/{song_title}.wav'
    data, sr = librosa.load(song_file, sr=None)
    
    for win_length in win_lengths:
        for min_length in min_lengths:
            # Get loop points based on a feature window and a minimum loop duration
            loop_begin, loop_end, score = find_loop_points(y=data, sr=sr,
                win_length=librosa.time_to_samples(win_length),
                min_length=librosa.time_to_samples(min_length)
            )[0]

            # Calculate the duration of the entire song in seconds
            song_duration_seconds = len(data[loop_begin:loop_end]) / sr
            # Print the duration of the entire song in minutes and seconds
            print(f'{song_title} (min_length-{min_length}, win_length-{win_length}) Duration: {int(song_duration_seconds // 60)} minutes {int(song_duration_seconds % 60)} seconds')

            loop = data[loop_begin:loop_end]

            new_loop_data = np.hstack([loop])
            sf.write(f'media/loop/{song_title}_(min_length-{min_length} win_length-{win_length}).wav', new_loop_data, sr)


