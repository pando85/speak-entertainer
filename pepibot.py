#!/usr/bin/env python2

import time
import telepot
from telepot.loop import MessageLoop
import speak
import json
import syslog
import argparse


def lee_secretos(configfile):
  with open(configfile, 'r') as f:
    return json.load(f)

def handle(msg):
  content_type, chat_type, chat_id = telepot.glance(msg)
  if chat_id not in secretos["authorized_ids"]:
      log = 'El usuario %s esta perdiendo el tiempo intentando que diga \"%s\"' %(telegram.getChat(chat_id)['first_name'],msg['text'])
      return
  if content_type == 'text':
    speak.reproduce_file(speak.get_text_to_speech_file(msg['text']))
    log = 'El usuario %s me ha obligado a decir "%s"' %(telegram.getChat(chat_id)['first_name'],msg['text'])
  syslog.syslog(log)


if __name__ == "__main__":

  parser = argparse.ArgumentParser()
  parser.add_argument("-c", "--config", required=True, help="Define el fichero json de configuracion del script")
  args = vars(parser.parse_args())

  secretos = lee_secretos(args["config"])
  telegram = telepot.Bot(secretos["token"])
  MessageLoop(telegram,handle).run_as_thread()

  while 1:
    secretos = lee_secretos(args["config"])
    time.sleep(300)

    