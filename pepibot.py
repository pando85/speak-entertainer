#!/usr/bin/env python2

import time
import telepot
from telepot.loop import MessageLoop
import speak
import yaml
import syslog

def handle(msg):
  content_type, chat_type, chat_id = telepot.glance(msg)
  if chat_id not in authorized_ids:
      log = 'El usuario %s esta perdiendo el tiempo intentando que diga \"%s\"' %(telegram.getChat(chat_id)['first_name'],msg['txt'])
      return
  if content_type == 'text':
    speak.reproduce_file(speak.get_text_to_speech_file(msg['text']))
    log = 'El usuario %s me ha obligado a decir \"%s\"' %(telegram.getChat(chat_id)['first_name'],msg['txt'])
  syslog.syslog(log)


if __name__ == "__main__":
  # leyendo variables de pepibot.yml
  stream = open("pepibot.yml","r")
  my_dict = yaml.load_all(stream)
  for key in my_dict:
    token = key['token']
    authorized_ids = key['authorized_ids']

  telegram = telepot.Bot(token)

  MessageLoop(telegram,handle).run_as_thread()
  while 1:
    time.sleep(1)

    