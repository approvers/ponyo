import json
from src.NEKO import send_neko
from src.DOG import send_DOG

with open('json/command.json',encoding="utf-8") as f:
    command = json.load(f)

async def choice_Message(message):
    # botならバイバイするのだ！
    if message.author.bot:
        return

    # Messageの内容
    content = message.content

    if content in command["NEKO"]:
        await send_neko(message)

    if content in command["DOG"]:
        await send_DOG(message)
