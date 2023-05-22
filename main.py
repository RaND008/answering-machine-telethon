import asyncio
import os
from telethon import TelegramClient, events, sync, utils
from telethon import functions, types
from mutagen.mp3 import MP3
import random as rand

# Получаем параметры для подключения к API по адресу:
# api_hash from https://my.telegram.org, under API Development.
api_id = 12345678
api_hash = '5373abe92ed21fe760dce52q478q54c6'
chat = -123456789 # Чат айди сами загуглите как искать

client = TelegramClient('komandos_kolya', api_id, api_hash)
file_govno = open('messages_from_chat.txt', 'r')
data = file_govno.readlines() # Читаем текстовый файл и построчно по элементам разбиваем в список

# генерация списка звуковых файлов #
directory = 'music'
files_mp3 = os.listdir(directory)
files_mp3_dir = [f'music/{files_mp3}' for files_mp3 in files_mp3]
# генерация списка звуковых файлов#


@client.on(events.NewMessage(chats=[chat]))
async def handler(event):
    #print(event.raw_text) # Выводим все что пишут в чат
    lol_trek = rand.choice(files_mp3_dir) # Выбираем случайный трек из папки
    # Узнаем длину передаваемого трека #
    f = MP3(lol_trek)
    time_mp3 = int(f.info.length)
    # Узнаем длину передаваемого трека #

    # Генерируем список для эмуляции голосового эквалайзера #
    audio_logarifm = []
    n = 500
    for i in range(n):
        audio_logarifm.append(rand.randint(1, 31))
    # Генерируем список для эмуляции голосового эквалайзера #
    kakashka = rand.randint(1, 1000)
    if kakashka > 900: # В зависимости от того какое число выпадет в переменную "kakashka" и зависит отправка голосового сообщения в чат
        async with client.action(chat, 'record-audio'):
            await asyncio.sleep(rand.randint(4, 15))
            await event.reply(file=lol_trek, attributes=[types.DocumentAttributeAudio(
                duration=time_mp3,
                voice=True,
                waveform=utils.encode_waveform(bytes(audio_logarifm) * 999)
            )])
    elif kakashka < 100: # В зависимости от того какое число выпадет в переменную "kakashka" и зависит отправка текстового сообщения в чат
        async with client.action(chat, 'typing'):
            datarand = rand.choice(data)
            await asyncio.sleep(rand.randint(15, 25))
            await event.reply(datarand)

client.start()
client.run_until_disconnected()

