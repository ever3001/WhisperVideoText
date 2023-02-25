from moviepy.video.io.VideoFileClip import VideoFileClip
import whispervideotext.video_file_clip_utils as vfc_utils

import os


def convert_mp4_to_mp3(video_path, audio_path):
    """
    Convert the given video file to an MP3 audio file using moviepy.
    """
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path, fps=44100, nbytes=2, bitrate='256k')


def start_conversion_mp4_to_mp3(video_path, audio_path):
    call_convert_mp4_to_mp3 = True
    # Check if the MP3 file already exists and prompt the user to overwrite it if it does
    if os.path.exists(audio_path):
        print(f"MP3 file {audio_path} already exists. Overwrite?")
        answer = input("y/n: ").lower()
        if answer == "n":
            call_convert_mp4_to_mp3 = False
    if call_convert_mp4_to_mp3:
        # Convert the video to MP3
        try:
            vfc_utils.convert_mp4_to_mp3(video_path, audio_path)
        except Exception as e:
            print(f"Error converting video to MP3: {e}")
            exit(1)
