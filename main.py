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
            embed=discord.Embed(title=new[0], description= f"{name} has caught " + new[0] + "!")
            list = ["aidan1888-Pikachu"]
            file = open("PokeDex.txt", "r")
            list = file.readlines()
            file.close()
            list.append(name + "-" + new[0])


            my_file = "PokeDex.txt"
            file = open(my_file, "w")
            z= 0
            v = len(list)
            st=""
            while z != v:
                file.write(list[z])
                z+=1
            await ctx.reply(list)
                
            



            
                    


                    


                    
                    
            #f.write(new[0])
            count = 2
            await ctx.reply(embed=embed)

            count=2
        elif prob == 1 and random.randrange(shiny) == 1:
            await ctx.reply("{name} has caught a SHINY " + new[0] + "!")
            count=2
        else:
            count=1


bot.run(TOKEN)