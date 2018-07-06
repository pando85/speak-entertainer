#!/usr/bin/env python
import binascii
import os
import pygame
import random
import subprocess

from gtts import gTTS


def generate_random_string(length):
    random_bits = os.urandom(length)
    random_string = binascii.hexlify(random_bits)
    return random_string.decode('utf-8')

def get_text_to_speech_file(text):
    tmp_file_path = '/tmp/{path}.mp3'.format( path = text)
    if not os.path.isfile(tmp_file_path):
        tts = gTTS(text=text, lang='es')
        tts.save(tmp_file_path)
    return tmp_file_path


if __name__ == "__main__":
    with open("/etc/speak/frases.txt") as file:
       sentences = [line for line in file]
    audio_files = []
    for sentence in sentences:
        audio_files.append(get_text_to_speech_file(sentence))

    pygame.mixer.init()
    pygame.mixer.music.load(random.choice(audio_files))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

