from pytube import YouTube
from pytube.helpers import safe_filename


def get_title_video(url):
    try:
        yt = YouTube(url)
        filename = safe_filename(yt.title)
        return filename
    except Exception as e:
        print(f"Error: {e}")


def download_audio(url, output_path='media'):
    try:
        yt = YouTube(url)
        title = get_title_video(url)
        audio_stream = yt.streams.get_audio_only()
        audio_stream.download(
            output_path=output_path,
            filename=f"{title}.{audio_stream.subtype}")
        print(f"{title} downloaded successfully to {output_path}")
        return title
    except Exception as e:
        print(f"Error: {e}")
