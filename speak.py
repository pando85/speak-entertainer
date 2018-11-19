""" speak-entertainer.

Usage:
    speak [-h] [-l LANGUAGE] [-t TEXT | -f FILE]

Options:
    -h --help                          Show this screen.
    -l LANGUAGE, --language LANGUAGE    Choose language. [default: es]
    -t TEXT, --text TEXT               Text to reproduce.
    -f FILE, --file FILE               File to take random line and reproduce it.
"""

import binascii
import docopt
import os
import pygame
import random
import sys
import subprocess
import hashlib
reload(sys)
sys.setdefaultencoding('utf8')

from gtts import gTTS
reload(sys)
sys.setdefaultencoding('utf8')


def generate_random_string(length):
    random_bits = os.urandom(length)
    random_string = binascii.hexlify(random_bits)
    return random_string.decode('utf-8')


def get_text_to_speech_file(text, language="es"):
    h = hashlib.new('sha512')
    h.update(text)
    _hash = h.hexdigest()
    tmp_file_path = '/tmp/{path}-{language}.mp3'.format(
        path = _hash , language = language)

    if not os.path.isfile(tmp_file_path):
        tts = gTTS(text=text, lang=language)
        tts.save(tmp_file_path)
    return tmp_file_path


def reproduce_file(_file):
    subprocess.call(["cvlc", "--play-and-exit", _file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if __name__ == "__main__":
    arguments = docopt.docopt(__doc__)
    if arguments["--text"]:
        reproduce_file(get_text_to_speech_file(arguments["--text"], arguments["--language"]))
        exit
    if arguments["--file"]:
        with open(arguments["--file"]) as file:
           sentences = [line for line in file]
        audio_files = []
        for sentence in sentences:
            audio_files.append(get_text_to_speech_file(sentence))

        reproduce_file(random.choice(audio_files))
        exit


