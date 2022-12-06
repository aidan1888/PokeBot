import discord
import random
import csv
from collections import defaultdict
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
        user = ctx.message.author
        name = str(user)
        name = name[:-5]
        count=0
        

        
        prob=random.randrange(num)
        if prob == 1 and random.randrange(shiny) != 1:
            list = ["aidan1888-Pikachu"]
            file = open("PokeDex.txt", "r")
            list = file.readlines()
            file.close()
            list.append(name + "-" + new[0] + "\n")


            my_file = "PokeDex.txt"
            file = open(my_file, "w")
            z= 0
            v = len(list)
            st=""
            while z != v:
                file.write(list[z])
                z+=1
            file.close()
            await ctx.reply(list)
            embed=discord.Embed(title=new[0], description= f"{name} has caught " + new[0] + "!")
            
            
            await ctx.reply(embed=embed)

            count=2
        elif prob == 1 and random.randrange(shiny) == 1:

            embed=discord.Embed(title=new[0], description= f"{name} has caught SHINY" + new[0] + "!")
            shinylist = ["\n"]
            file = open("ShinyDex.txt", "r")
            shinylist = file.readlines()
            file.close()
            shinylist.append(name + "-*" + new[0] + "*\n")


            myFile = "ShinyDex.txt"
            file = open(my_file, "w")
            z= 0
            v = len(shinylist)
            st=""
            while z != v:
                file.write(shinylist[z])
                z+=1
            file.close()
            await ctx.reply(shinylist)
            file = discord.File("C:/Users/aidan/Desktop/PokeBot/shiny.png", filename="shiny.png")
            embed.set_image(url="attachment://shiny.png")
            
            await ctx.reply(file=file, embed=embed)
            
            count=2
        else:
            count=1
@bot.group(with_app_command=True)
async def PokeDex(ctx):
    user = ctx.message.author
    name = str(user)
    name = name[:-5]
    file = open("PokeDex.txt", "r")
    list = file.readlines()
    newlist = []
    nLen=len(name) + 1
    for st in list:
        if st.startswith(name) and st not in newlist:
            st=st[nLen:]
            st=st.strip("\n")   
            if st not in newlist:
                newlist.append(st)
    
    embed=discord.Embed(title="PokeDex", description= f" has caught by {name}\n".join(newlist) + "has been caught by {name} so far.")
    file = discord.File("C:/Users/aidan/Desktop/PokeBot/dex.png", filename="shiny.png")
    embed.set_image(url="attachment://dex.png")
            
    await ctx.reply(file=file, embed=embed)
    


bot.run(TOKEN)