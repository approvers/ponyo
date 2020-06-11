import discord
from discord.ext import tasks
import no_git_token
import src.Message


class Client(discord.Client):

    def __init__(self):
        super().__init__()

    def run(self):
        TOKEN = no_git_token.TOKEN
        super().run(TOKEN)

    async def on_ready(self):
        print("bot起動なのだ！")

    async def on_message(self, message: discord.Message):
        await src.Message.choice_Message(message)

