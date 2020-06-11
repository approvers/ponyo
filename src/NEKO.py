import os
import random
import discord

NEKO_list = ["にゃん",
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
files_name = "pic/NEKO"
files = os.listdir(files_name)
NEKO_jpg = [f for f in files if os.path.isfile(os.path.join(files_name, f))]


# Messageを送信！！！
async def send_neko(message):
    await message.channel.send(random.choice(NEKO_list))
    await message.channel.send(file=discord.File('pic/NEKO/%s' % random.choice(NEKO_jpg)))
