[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# WhisperVideoText

**WhisperVideoText** is a Python script that extracts text from videos using the Whisper library. The script first converts the video file to an MP3 audio file using FFmpeg, and then uses the Whisper library to transcribe the audio to text. The resulting text is going to be saved in a text file.

## Installation

Install whispervideotext using PyPi:
``` bash
$ python3 -m pip install --upgrade git+https://github.com/ever3001/WhisperVideoText.git
```

Install whispervideotext from source:
```bash
$ git clone https://github.com/ever3001/WhisperVideoText.git
$ cd WhisperVideoText
$ pip3 install .
```

## Usage

```bash
whispervideotext [-h] [-o OUTPUT_MP3] [-s OUTPUT_TXT] [-m {tiny,base,small,medium,large}] input_video

Convert MP4 video to MP3 audio and transcribe the result

positional arguments:
  input_video           path to input MP4 video file

options:
  -o OUTPUT_MP3, --output_mp3 OUTPUT_MP3
                        path to save the MP3 audio file
  -s OUTPUT_TXT, --output_txt OUTPUT_TXT
                        path to save the script file
  -m {tiny,base,small,medium,large}, --model {tiny,base,small,medium,large}
                        choose the size of the speech recognition model
```

## Contribute

If you would like to contribute, please see the [instructions](./CONTRIBUTING.md).

## License

This project is licensed under the **Apache 2.0 license** - see the [LICENSE](./LICENSE) file for details.