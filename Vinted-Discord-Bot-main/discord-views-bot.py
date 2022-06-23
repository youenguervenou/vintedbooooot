import discord
from discord.ext import commands
import requests
from random import randint
import random
import time


requests.packages.urllib3.disable_warnings()

TOKEN = 'ODk0MjU0MTM1MzM0MDI3Mjk0.GqhKvN.QQB1nDC2lUnTeL_V3We1h_c8yGDLW9s6mO_lUs'

client = discord.Client() 


@client.event
async def on_message(message):
    
    if message.content.startswith('!vintedviews'):
        old = message.content
        url = old.replace("!vintedviews", "").strip()
        print ("Viewer started")
        await message.channel.send("ajout de 50 vues a l'article {}.".format(message.author))
        headers1 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            }
        
        for i in range(50):
            try:
                r =  requests.get(url,headers=headers1,verify=False,timeout=5)
                if r.status_code == 200:
                    print ("Viewed successfully")
               
            except Exception as e:
                print(e)
        
        embed = discord.Embed(title="", color=0x00ff00)
        await message.channel.send("sucess {}.".format(message.author))
        


    if message.content == ('!help'):
        embed = discord.Embed(title="", color=0x00ff00)
        embed.add_field(name="Give 50 views to an item", value="!vintedviews ", inline=True)
    


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

while True:
    client.run(TOKEN)
