import os
import random
import discord

NEKO_LIST = ["にゃん",
             "にゃおーん",
             "にゃんにゃん",
             "にゃん.....",
             "にゃん><",
             "にゃんにゃんにゃーん",
             "ワン！",
             "ねこです。 よろしくおねがいします。",
             "ねこだよ",
             "ねこかも",
             "ねこねこ",
             "にゃん",
             "ねっこ！！！",
             "ヌコ",
             "いっそうは動物好きになれ",
             "にゃん💕",
             "にゃーおーーーん"]

# ファイルの中の画像名取得
FILES_NAME = "pic/NEKO"
files = os.listdir(FILES_NAME)
NEKO_jpg = [f for f in files if os.path.isfile(os.path.join(FILES_NAME, f))]


# Messageを送信！！！
async def send_neko(message):
    await message.channel.send(random.choice(NEKO_LIST))
    NEKO_file_name = discord.File('pic/NEKO/%s' % random.choice(NEKO_jpg))
    await message.channel.send(file=NEKO_file_name)
