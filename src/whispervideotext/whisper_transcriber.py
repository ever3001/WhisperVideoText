from threading import Thread
import whispervideotext.utils as wvt_utils
import whisper
import os


def transcribe(audio_path, model, output_txt):
    # Transcribe the MP3 file using the whisper library
    # test if the file mp3 exists
    if not os.path.exists(audio_path):
        print(f"{audio_path} does not exist")
        exit(1)
    try:
        print(
            f"\r\nTranscribing MP3 file: {audio_path} using model {model}")
        # Boolean flag to indicate when animation is done
        done_flag = False
        # Start the animation in a separate thread
        t = Thread(target=wvt_utils.show_terminal_animation, args=(lambda: done_flag, ))
        model = whisper.load_model(model)
        t.start()
        result = model.transcribe(audio_path)
        # Write the transcription result to a text file
        with open(output_txt, 'w') as f:
            f.write(result["text"])
        print(f"Transcription result saved to: {output_txt}")
    except Exception as e:
        print(f"Error transcribing MP3 file: {e}")
        done_flag = True
        exit(1)

    done_flag = True
