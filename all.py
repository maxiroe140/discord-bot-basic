#------imports-----#

import discord 
import discord 
from discord.ext import commands,tasks
import asyncio
import discord.ext.commands 
import discord.utils

#-----einstelungen-----#

token = "DEIN TOKEN"
colors = ['0xFFE4E1', '0x00FF7F', '0xD8BFD8', '0xDC143C', '0xFF4500', '0xDEB887', '0xADFF2F', '0x800000', '0x4682B4', '0x006400', '0x808080', '0xA0522D', '0xF08080', '0xC71585', '0xFFB6C1', '0x00CED1']

bot = commands.Bot(command_prefix='+' , intents=discord.Intents.al())


@tasks.loop(minutes=15)
async def status_task():
        await bot.change_presence(activity=discord.Game(name="Status"))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('nicht genügend angaben')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("keinerlei rechte hehe ")

#----commands----#

@client.command()
async def say(ctx, *,message):
await ctx.message.delete()
embed=discord.Embed(description="(description=message"color (colors))
await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send('gebannát wegen {reason}')


@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send('gebannát wegen {reason}')

@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)
    await ctx.send(f'gekickt')





#----runs---#

client.run(token)