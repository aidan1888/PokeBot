import discord
import random
from discord import app_commands
from discord.ext import commands

TOKEN = ""

with open("TOKEN.txt", "r") as file:
    TOKEN = file.readline()


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents)

bot = Bot() 