import discord
from discord.ext import tasks
from no_git_token import TOKEN
from src.Message import choice_Message


class Client(discord.Client):

    def __init__(self):
        super().__init__()

    def run(self):
        TOKEN
        super().run(TOKEN)

    async def on_ready(self):
        print("bot起動なのだ！")

    async def on_message(self, message: discord.Message):
        await choice_Message(message)

