import discord
import random
import csv
from collections import defaultdict
from discord.ext import commands

client = discord.Client()

TOKEN = ""

with open("TOKEN.txt", "r") as file:
    TOKEN = file.readline()

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        #intents.messages_content = True
        super().__init__(command_prefix="!", intents=intents)

bot = Bot()

pfp_path = "C:/Users/aidan/Desktop/PokeBot/pokeball.png"
fp = open(pfp_path, 'rb')
pfp = fp.read()


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    channel = bot.get_channel(1049215170351747074)

    await channel.send("I'm back online!")
    
    
    await bot.user.edit(avatar=pfp)

@bot.group(with_app_command=True)
async def name(ctx, arg):
    
    nameLen = len(arg)
    user = ctx.message.author
    name = str(user)
    name = name[:-5]
    file = open("PokeDex.txt", "r")
    list = file.readlines()
    newlist = []
    total=0
    nLen=len(name) + 1
    for st in list:
        if st.startswith(arg):
            total+=1
            st=st[nameLen:]
            st=name + st

    my_file = "PokeDex.txt"
    file = open(my_file, "w")
    z= 0
    v = len(list)
    st=""
    while z != v:
        file.write(list[z])
        z+=1
    file.close()


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
        if prob == 1 and random.randrange(shiny) != 1 and new[0] != "nothing":
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

            #await ctx.reply(list)

            embed=discord.Embed(title=new[0], description= f"{name} has caught " + new[0] + "!")
            file=discord.File("C:/Users/aidan/Desktop/PokeBot/Pokemon Dataset/" + new[0] + ".png", filename=new[0] + ".png")
            embed.set_image(url="attachment://" + new[0] + ".png")

            
            
            await ctx.reply(file=file, embed=embed)

            count=2
        elif prob == 1 and random.randrange(shiny) == 1 and new[0] != "nothing":

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

        elif new[0] == "nothing":
            embed=discord.Embed(title=new[0], description= f"{name} caught " + new[0] + "!")
            file=discord.File("C:/Users/aidan/Desktop/PokeBot/Pokemon Dataset/" + new[0] + ".png", filename=new[0] + ".png")
            embed.set_image(url="attachment://" + new[0] + ".png")
            await ctx.reply(file=file, embed=embed)

        elif prob != 1:
            embed=discord.Embed(title=new[0] + " has fled!!", description= f"{name} almost caught " + new[0] + ", but it fled!")
            file=discord.File("C:/Users/aidan/Desktop/PokeBot/Pokemon Dataset/fled.gif", filename="fled.gif")
            embed.set_image(url="attachment://fled.gif")
            await ctx.reply(file=file, embed=embed)

        else:
            count=1


@bot.group(with_app_command=True)
async def pokedex(ctx):
    user = ctx.message.author
    name = str(user)
    name = name[:-5]
    file = open("PokeDex.txt", "r")
    list = file.readlines()
    newlist = []
    caught=0
    total=0
    nLen=len(name) + 1
    for st in list:
        if st.startswith(name) and st not in newlist:
            total+=1
            st=st[nLen:]
            st=st.strip("\n")
            if st not in newlist:
                newlist.append(st)
                caught+=1
    
    embed=discord.Embed(title="---------PokeDex---------", description= f" has caught by {name}\n".join(newlist) + " has been caught by " + name + " so far.")
    file = discord.File("C:/Users/aidan/Desktop/PokeBot/dex.png", filename="dex.png")
    embed.set_image(url="attachment://dex.png")
            
    await ctx.reply(file=file, embed=embed)
    embed=discord.Embed(title="------Catch History------", description= f"{name} has caught {total} pokemon in total\n{name}'s PokeDex Completion Progress: {caught}/905.\nGotta catch 'em all!")
    await ctx.reply(embed=embed)

@bot.group(with_app_command=True)
async def Shinydex(ctx):
    user = ctx.message.author
    name = str(user)
    name = name[:-5]
    file = open("ShinyDex.txt", "r")
    list = file.readlines()
    newlist = []
    nLen=len(name) + 1
    caught=0
    total=0
    for st in list:
        if st.startswith(name) and st not in newlist:
            total+=1
            st=st[nLen:]
            st=st.strip("\n")
            if st not in newlist:
                newlist.append(st)
                caught+=1
    if newlist ==[]:
        embed=discord.Embed(title="------======Shiny PokeDex======------", description= f" You have not caught any shinies yet.")
    else:
        embed=discord.Embed(title="------======Shiny PokeDex======------", description= f" has been caught by {name}\n".join(newlist) + "has been caught by {name}.")
        
    file = discord.File("C:/Users/aidan/Desktop/PokeBot/shinydex.png", filename="shinydex.png")
    embed.set_image(url="attachment://shinydex.png")
            
    await ctx.reply(file=file, embed=embed)
    embed=discord.Embed(title="------======Catch History======------", description= f"{name} has caught {total} shinies in total\n{name}'s ShinyDex Completion Progress: {caught}/905 shinies.\nGotta catch 'em all!")
    await ctx.reply(embed=embed)


bot.run(TOKEN)