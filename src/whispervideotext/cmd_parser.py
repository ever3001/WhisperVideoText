import argparse


def init_argparse():
    """
    Initialize the arguments for the script.
    """
    parser = argparse.ArgumentParser(
        "whispervideotext",
        description='Convert MP4 video to MP3 audio and transcribe the result',
        add_help=True
    )
    parser.add_argument(
        'input_video',
        help='path to input MP4 video file',
        type=str
    )
    parser.add_argument(
        '-o',
        '--output_mp3',
        dest='output_mp3',
        default='output_mp3.mp3',
        help='path to save the MP3 audio file',
        type=str
    )
    parser.add_argument(
        '-s',
        '--output_txt',
        dest='output_txt',
        default='script.txt',
        help='path to save the script file',
        type=str
    )
    parser.add_argument(
        '-m',
        '--model',
        dest='model',
        default='base',
        choices=['tiny', 'base', 'small', 'medium', 'large'],
        help='choose the size of the speech recognition model',
        type=str
    )

    return parser
