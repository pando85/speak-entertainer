#!/usr/bin/env python2

import time
import telepot
from telepot.loop import MessageLoop
import speak
import yaml

stream = open("pepibot.yml","r")

my_dict = yaml.load_all(stream)

for key in my_dict:
  token = key['token']
  authorized_ids = key['authorized_ids']


def handle(msg):
  content_type, chat_type, chat_id = telepot.glance(msg)
  if chat_id not in authorized_ids:
      return
  if content_type == 'text':
    speak.reproduce_file(speak.get_text_to_speech_file(msg['text']))
    #telegram.sendMessage(chat_id, msg['text'])
    
if name == "main":
  telegram = telepot.Bot(token)

  MessageLoop(telegram,handle).run_as_thread()
  while 1:
    time.sleep(1)