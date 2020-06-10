import src.NEKO
import src.command
import src.DOG


async def choice_Message(message):
    # botならバイバイするのだ！
    if message.author.bot:
        return

    # Messageの内容
    message_main = message.content

    if message_main in src.command.message_list_NEKO:
        await src.NEKO.send_neko(message)

    if message_main in src.command.message_list_DOG:
        await src.DOG.send_DOG(message)
