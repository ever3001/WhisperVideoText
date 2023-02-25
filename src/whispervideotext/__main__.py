#!/usr/bin/env python3

import whispervideotext.cmd_parser as cmd_parser
import whispervideotext.whisper_transcriber as whisper_transcriber
import whispervideotext.video_file_clip_utils as vfc_utils

import os

def main():

    parser = cmd_parser.init_argparse()
    args = parser.parse_args()

    # Convert the MP4 video file to MP3 audio file
    vfc_utils.start_conversion_mp4_to_mp3(args.input_video, args.output_mp3)
    # Transcribe the MP3 file using the whisper library
    whisper_transcriber.transcribe(
        os.path.abspath(args.output_mp3),
        args.model,
        os.path.abspath(args.output_txt)
    )


if __name__ == '__main__':
    main()
