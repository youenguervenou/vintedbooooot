import discord
from discord.ext import commands
default_intents = discord.Intents.default()
default_intents.members = True 
import random
import asyncio
PREFIX = ("?")
bot = commands.Bot(command_prefix=PREFIX, description='Hi')
client = commands.Bot(command_prefix=PREFIX, description='Hi')
import datetime

from discord_slash import ButtonStyle, SlashCommand
from discord_slash.utils.manage_components import *
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option, create_choice, create_permission
from discord_slash.model import SlashCommandPermissionType
slash = SlashCommand(bot, sync_commands = True)

from discord.ext import commands
from discord.utils import get

from discord.ext.commands import has_permissions, MissingPermissions

guilds = [986923782193160192]
@bot.event
async def on_guild_join(guild):
    #append the guild id when it joins a new server
    guilds.append(guild.id)

@bot.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.watching, name="/help")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("le bot est prêt")

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send("Mmmmmmh, j'ai bien l'impression que cette commande n'existe pas :/")

	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send("Il manque un argument.")
	elif isinstance(error, commands.MissingPermissions):
		await ctx.send("Vous n'avez pas les permissions pour faire cette commande.")
	elif isinstance(error, commands.CheckFailure):
		await ctx.send("Oups vous ne pouvez pas utilisez cette commande.")
	if isinstance(error.original, discord.Forbidden):
		await ctx.send("Oups, je n'ai pas les permissions nécéssaires pour faire cette commmande")

@slash.slash(name="size_femme", guild_ids=guilds, description="voir les tailes femme us en eu ")
async def size_femme(ctx):
    await ctx.send("https://www.sports-loisirs.fr/img/cms/guides%20pointure/Pointures-femme-Nike.jpeg")

@slash.slash(name="size_homme", guild_ids=guilds, description="voir les tailes homme us en eu ")
async def size_homme(ctx):
    await ctx.send("https://www.sports-loisirs.fr/img/cms/guides%20pointure/Pointures-homme-nike.jpeg")

@slash.slash(name="raffle", guild_ids=guilds, description="voir les sites qui prélèvent ou non lors de raffle")
async def raffle (ctx):
    embed =  discord.Embed (title = ("Guides des prélevements pour les raffles"),description = (" "))
    embed.set_author(name=f"{ctx.author}", icon_url=f"{ctx.author.avatar_url}")
    embed.set_thumbnail(url="https://o.remove.bg/downloads/ed7e9564-dfc6-4ae6-aec9-957856257ae3/image-removebg-preview.png")
    embed.add_field(name = ("__sites qui prélèvent__"),value=("-consortuim\n""-Cornerstreet\n""-Footpatrol\n" "-GrosBaskets\n" "-Hanon\n" "-kickz\n" "-JD sport\n" "-Seventstore\n" "-size\n" "-Slam Jam\n"), inline=False)  
    embed.add_field(name = ("__sites qui ne prélèvent pas__"),value=("-afew\n" "-Basket4Ballers\n" "-BSTN\n""-Courir\n""-END\n" "-Fenom\n" "-Footshop\n" "-Goodhood\n" "-Kith\n" "-Noirfonce\n" "-One Block Down\n" "-shinzo\n" "-Sivasdescalzo\n" "-SNS\n" "-4 elementos\n" "-adidas CONFIRMED \n" "-nike \n" "-SNKRS\n"), inline=False)
    embed.set_footer(text="raffle | FlashTools")
    await ctx.send(embed = embed)

class MyHelpCommand(commands.MinimalHelpCommand):
    def get_command_signature(self, command):
        return '{0.clean_prefix}{1.qualified_name} {1.signature}'.format(self, command)

class MyCog(commands.Cog):
    def __init__(self, bot):
        self._original_help_command = bot.help_command
        bot.help_command = MyHelpCommand()
        bot.help_command.cog = self

    def cog_unload(self):
        self.bot.help_command = self._original_help_command

bot.remove_command("help")

@slash.slash(name="help", guild_ids=guilds, description="commande d'aide ")
async def help(ctx):
    embed = discord.Embed(title= "**help command**", description= " ", color=0xF01515)
    embed.add_field(name=('voici la liste des commande disponible grâce à FlashTools'), value=('`size_homme` : pour voir la taille us en eu \n' "`size_femme` : pour voir la taille us en eu \n" "`raffle` : pour voir les sites qui prélèvent où non lors de raffle \n" "`embed` : pour créer un embed custom \n" "`version` : pour voir la version du bot et les mises à jour \n" "`wtb` : pour faire une annonce WantToBuy \n" "`wts` : pour faire une annonce WantToSell \n" "`!vintedview + url` : ajouter des vues vinted à une annonces"))
    embed.set_footer(text="help command | FlashTools")
    await ctx.send(embed = embed)

@slash.slash(name="version", guild_ids=guilds, description="voir la version du bot")
async def version(ctx):
    # Version command that contains the current version number and recent changes made
    ver = discord.Embed(color = 0x7289da)
    ver.set_author(name = 'Notes de mise à jour', icon_url= 'https://cdn.discordapp.com/attachments/985156889170018318/986295957090086932/unknown.png')
    ver.add_field(name = 'Version: 2.1.4', value = f"• l'interface du bot a été revu • ajout de command slash • modification des sites raffle • **le bot est désormais hébergé !** • ajout de la commande /embed pour créer des embed personnalisés • commande ?lock et ?unlock pour bloquer et débloquer un salon " , inline= False)
    await ctx.send(embed = ver)

@slash.slash(name="embed", guild_ids=guilds, description="envoyer un message en embed")
async def embed(ctx, title, name, field, member = discord.Member,):
    title = discord.Embed(title= f"{title}", description= " ", color=0x1ABC9C)
    field = title.add_field(name=(f'{name}'), value=(f"{field}"))
    title.set_footer(text= ctx.author.display_name, icon_url= ctx.author.avatar_url)
    await ctx.send(embed=title)

@slash.slash(name="lock", guild_ids=guilds, description="bloquer un salon")
@commands.has_permissions(manage_roles=True, ban_members=True)
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send( ctx.channel.mention + " ***est maitenant lock***")


@slash.slash(name="unlock", guild_ids=guilds, description="débloquer un salon")
@commands.has_permissions(manage_roles=True, ban_members=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send(ctx.channel.mention + " ***est maintenant unlocked.***")

@slash.slash(name="wtb", guild_ids=guilds, description="Want To Buy")
async def wtb(ctx, sku, name, prix, etat, size , envoie, ville,):
    id = ctx.guild.id


    embed = discord.Embed(title= "WTB", description= f"**{name}**", color=0x1ABC9C)
    embed.set_author(name=f"{ctx.author.display_name}", icon_url=f"{ctx.author.avatar_url}")
    prix = embed.add_field(name=("💰 Prix souhaité "), value=(f"> {prix}€"), inline=True)
    etat= embed.add_field (name=("🟢 Etat souhaité"), value = (f"> {etat}"))
    size = embed.add_field(name=("📏 Size(s)"), value=(f"> {size}"))
    envoie = embed.add_field(name=("🚚 Envoie possible"), value = (f"> {envoie}"))
    ville = embed.add_field(name=("📍 Ville"), value=(f"> {ville}"))
    embed.add_field(name=("💬 Contact"), value= (f"> ||{ctx.author}||"))
    time = datetime.datetime.utcnow()
    embed.add_field(name="⏱ Mis(e) en ligne le : ", value =(f"{time}"))
    embed.set_footer(text=f" | sku : {sku}", icon_url="https://cdn.discordapp.com/attachments/927637329693257780/985942920844689438/cintre.png")
    await ctx.send(embed=embed)
@slash.slash(name="wts", guild_ids=guilds, description="Want To Sell")
async def wtb(ctx, sku, name, prix, etat, size , envoie, ville, ):
    embed = discord.Embed(title= "WTS", description= f"**{name}**", color=0x1ABC9C)
    embed.set_author(name=f"{ctx.author.display_name}", icon_url=f"{ctx.author.avatar_url}")
    prix = embed.add_field(name=("💰 Prix"), value=(f"> {prix}€"), inline=True)
    etat= embed.add_field (name=("🟢 Etat"), value = (f"> {etat}"))
    size = embed.add_field(name=("📏 Size(s)"), value=(f"> {size}"))
    envoie = embed.add_field(name=("🚚 Envoie possible"), value = (f"> {envoie}"))
    ville = embed.add_field(name=("📍 Ville"), value=(f"> {ville}"))
    embed.add_field(name=("💬 Contact"), value= (f"> ||{ctx.author}||"))
    time = datetime.datetime.utcnow()
    embed.add_field(name="⏱ Mis(e) en ligne le : ", value =(f"{time}"))
    embed.set_footer(text=f" | sku : {sku}", icon_url="https://cdn.discordapp.com/attachments/927637329693257780/985942920844689438/cintre.png")
    await ctx.send(embed=embed)

@slash.slash(name="unmute", guild_ids=guilds, description="unmute un membre")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muet")

   await member.remove_roles(mutedRole)
   await member.send(f" tu as été unmute de : {ctx.guild.name}")
   embed = discord.Embed(title="unmute", description=f" {member.mention} a été unmute",colour=discord.Colour.light_gray())
   await ctx.send(embed=embed)

@slash.slash(name="mute", guild_ids=guilds, description="mute un membre")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muet")

   await member.add_roles(mutedRole)
   await member.send(f" tu as été mute de : {ctx.guild.name}")
   embed = discord.Embed(title="mute", description=f" {member.mention} a été mute",colour=discord.Colour.light_gray())
   await ctx.send(embed=embed)

bot.run('ODk0MjU0MTM1MzM0MDI3Mjk0.GqhKvN.QQB1nDC2lUnTeL_V3We1h_c8yGDLW9s6mO_lUs')