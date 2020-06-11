import os
import random
import discord

DOG_LIST = ["わん！",
            "わおーーん",
            "わんわん！",
            "わん！！！",
            "わん><",
            "わん......",
            "いっそうは動物を好きになるニャン",
            "わおん！",
            "いぬです。よろしくおねがいします",
            "いっぬ",
            "わんわん！",
            "わんわんわん！",
            "わん？",
            "わん！",
            "わおん！",
            "わわん",
            "わん❤"]

# ファイルの中の画像名取得
FILES_NAME = "pic/DOG"
files = os.listdir(FILES_NAME)
DOG_jpg = [f for f in files if os.path.isfile(os.path.join(FILES_NAME, f))]


# Messageを送信！！！
async def send_DOG(message):
    await message.channel.send(random.choice(DOG_LIST))
    DOG_file_name = discord.File('pic/DOG/%s' % random.choice(DOG_jpg))
    await message.channel.send(file = DOG_file_name)
