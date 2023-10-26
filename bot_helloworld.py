#!/usr/bin/python3
#coding: utf-8

import telepot, time

def principal(msg):
    content_type, cha_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        chat_id = msg['chat']['id']
        mensagem = msg['text']

    if mensagem == 'oi' :
        bot.sendMessage(chat_id, 'Ola Mundo!')

bot = telepot.Bot('6976983950:AAHyIZYMuNMBVxbNn3z4hvrYz7LB-Fep2EQ')

bot.message_loop(principal)

while True:
    time.sleep(5)