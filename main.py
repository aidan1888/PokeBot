import discord
import random
from discord.ext import commands
TOKEN = ""

with open("TOKEN.txt", "r") as file:
    TOKEN = file.readline()

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        #intents.messages_content = True
        super().__init__(command_prefix="!", intents=intents)

bot = Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.group(with_app_command=True)
async def catch(ctx):
    with open("pokemon.txt") as file:
        for line in file:
            pokemonList = file.readlines()
        
    




    
    count=1
    final =""
    name = ""
    while (count == 1):
        count =1
        new=random.choice(pokemonList)
        new=new.split()
        if len(new) == 2:
            num=new[1]
        elif len(new) == 3:
            num=new[2]
        elif len(new) == 4:
            num=new[2]
        num=int(num)
        shiny=num*6
        name = ctx.message.author
        name = str(name)
        long = len(name)
        name = name[4:len]
        count=0
        

        
        prob=random.randrange(num)
        if prob == 1 and random.randrange(shiny) != 1:
            embed=discord.Embed(title=new[0], description= f"{final} has caught " + new[0] + "!")
            
            
            #f = open(user + ".txt", "a")
            #f.append(new[0])
            await ctx.reply(embed=embed)

            count=2
        elif prob == 1 and random.randrange(shiny) == 1:
            await ctx.reply("{final} has caught a SHINY " + new[0] + "!")
            count=2
        else:
            count=1


bot.run(TOKEN)