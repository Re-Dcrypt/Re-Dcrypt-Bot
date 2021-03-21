version = "Re-dcrypt Bot v0.9.8 Beta"


print(f'Starting {version}...')

import discord
from discord.ext import commands
#import Cipher #pip install CipherModule
import string
import os
import base64
import binascii
from art import *
import asyncio
from discord_slash import SlashCommand
from utils import *
import typing



help_dict={
	'Prefix':'&?' ,
	'Commands': 'Below are the commands you can use with this bot',
	'Caesar': ['```&?caesar [key] [code]\n&?caesar [code] (This will brute force with all keys)```' , 'For eg. `&?caesar 5 Sjajw Ltssf Lnaj Dtz Zu`'],
	'Vigenere': ['```&?vigenere_encode [key] [code]\n&?vigenere_decode [key] [code]```', 'For eg `&?vigenere_decode rick ymnvf eqbcl`'],
	'null':["```&?null [text]```","For eg. `&?null george owns one green little elephant`"],
	'a1z26': ['```&?a1z26 [code] (can be numbers/alphabets)```', "For eg. `&?a1z26 7 15 15 7 12 5` or `&?a1z26 Microsoft `"],
	'base64':['```&?b64_decode [code]\n&?b64_encode [code]```','For eg `&?base64_decode UmUtRGNyeXB0` or `&?base64_encode monke`'],
	'atbash':['```&?atbash [code]```', "For eg. `&?atbash blf pmld gsv ifovh & hl wl r`"],
	'morse': ['```&?morse [code/text]\n(This will automatically decode the morse & encode the text)```', "For eg. `&?morse  ... --- -- . - .... .. -. --.  / .--- ..- ... -  / .-.. .. -.- .  / - .... .. ...`"],
	'tap':['```&?tap [code/text] \n(This will automatically decode the tap code & encode the text)```',"For eg. `&?tap ... .... ... ..... . ..... ... ...  / .. ... . . ... ..... ... ..... .. .... ... ... . ..... .... ... .... ... `"],
	'bacon':["```&?bacon_encode [text]\n&?bacon_decode [code]\n&?bacon_encode [complete] [text]\n&?bacon_decode [complete] [code]\n\nNote: By default Bacon cipher will decrypt/encrypt in the standard (I=J, U=V) form. If you need to encrypt/decrypt in complete form of bacon cipher then you need to mention it.```","For eg. `&?bacon_decode AABBA ABBAB ABBAB AABBA ABABA AABAA ` or `&?bacon_encode Google`"],
	'reverse':['```&?reverse [text]```', "For eg. `&?reverse olleh`"],
	'slash':"```You can use slash commands as well. They are much more simpler to use & don't require you to remember the commands. The format is predifened & you just have to select the things.```"

}

def helpcmd(arg):
	embed = discord.Embed(title='Bot Help', colour=discord.Colour(0x39ff14))
	embed.set_author(name='Re-Dcrypt', icon_url='https://i.imgur.com/ynad6vI.png')
	if arg==None:
		embed.add_field(name='Prefix', value='&?', inline=True)
		embed.add_field(name='Commands:',value=f'{help_dict["Commands"]}')
		embed.add_field(name='Caesar Cipher Decode', value=f"{help_dict['Caesar'][0]}", inline=False)
		embed.add_field(name='Vigenere Cipher', value=f"{help_dict['Vigenere'][0]}",inline=False)
		embed.add_field(name='Null Cipher', value=f"{help_dict['null'][0]}",inline=False)

		embed.add_field(name='a1z26',value=f"{help_dict['a1z26'][0]}", inline=False)
		embed.add_field(name='Base64',value=f"{help_dict['base64'][0]}",inline=True)
		embed.add_field(name='Atbash',value=f"{help_dict['atbash'][0]}", inline=True)
		embed.add_field(name='Morse Code',value=f"{help_dict['morse'][0]}",inline=False)
		embed.add_field(name='Tap Code',value=f"{help_dict['tap'][0]}")
		embed.add_field(name='Bacon/Baconian Cipher',value=f"{help_dict['bacon'][0]}", inline=False)
		embed.add_field(name='Text Reverse',value=f"{help_dict['reverse'][0]}", inline=True)
		embed.add_field(name='Feedback/Suggestion',value='''```&?feedback [your feedback/suggestion]```''',inline=True)
		embed.add_field(name='Note',value='The Prefix `&?` is only required in servers. All the commands will work without the prefix in the bots DM.',inline=False)
		embed.add_field(name='Slash Commands',value="""```diff\n+ Most of the above commands are available as slash commands as well. For Slash commands, you just have to type `/` and then you will see multiple options for the commands. The format is also predefined in the slash commands so you don't have to remember anything.\n```""")
		embed.add_field(name='About:',value='''***Re-Dcrypt Bot v0.9.8 Beta***\n<a:BlobDiscord:779402415916580864> [Invite Me](https://discord.com/api/oauth2/authorize?client_id=775629409494630410&permissions=346176&redirect_uri=https%3A%2F%2Fbot.redcrypt.ml&scope=bot%20applications.commands)\n<a:redcryptexcited:781090077748494336> [Our Community Server](https://discord.gg/c68aWWMruT)''',inline=False)

	elif arg.lower().startswith('caesar'):
		embed.add_field(name='Caesar Cipher Decode', value=f"{help_dict['Caesar'][0]}\n {help_dict['Caesar'][1]}", inline=False)
        #embed.add_field(name='Note',value='The Prefix `&?` is only required in servers. All the commands will work without the prefix in the bots DM.',inline=False)
		embed.add_field(name='Slash Commands', value=f"{help_dict['slash']}", inline=False)


	elif arg.lower().startswith('vigenere'):
		embed.add_field(name='Vigenere Cipher', value=f"{help_dict['Vigenere'][0]}\n {help_dict['Vigenere'][1]}", inline=False)
        #embed.add_field(name='Note',value='The Prefix `&?` is only required in servers. All the commands will work without the prefix in the bots DM.',inline=False)
		embed.add_field(name='Slash Commands', value=f"{help_dict['slash']}", inline=False)

	elif arg.lower().startswith('a1z26'):
		embed.add_field(name='a1z26', value=f"{help_dict['a1z26'][0]}\n {help_dict['a1z26'][1]}", inline=False)
        #embed.add_field(name='Note',value='The Prefix `&?` is only required in servers. All the commands will work without the prefix in the bots DM.',inline=False)
		embed.add_field(name='Slash Commands', value=f"{help_dict['slash']}", inline=False)

	elif arg.lower().startswith('base64'):
		embed.add_field(name='Base64', value=f"{help_dict['base64'][0]}\n {help_dict['base64'][1]}", inline=False)
        #embed.add_field(name='Note',value='The Prefix `&?` is only required in servers. All the commands will work without the prefix in the bots DM.',inline=False)
		embed.add_field(name='Slash Commands', value=f"{help_dict['slash']}", inline=False)

	elif arg.lower().startswith('null'):
		embed.add_field(name='null', value=f"{help_dict['null'][0]}\n {help_dict['null'][1]}", inline=False)
        #embed.add_field(name='Note',value='The Prefix `&?` is only required in servers. All the commands will work without the prefix in the bots DM.',inline=False)
		embed.add_field(name='Slash Commands', value=f"{help_dict['slash']}", inline=False)

	elif arg.lower().startswith('atbash'):
		embed.add_field(name='Atbash Cipher', value=f"{help_dict['atbash'][0]}\n {help_dict['atbash'][1]}", inline=False)
        #embed.add_field(name='Note',value='The Prefix `&?` is only required in servers. All the commands will work without the prefix in the bots DM.',inline=False)
		embed.add_field(name='Slash Commands', value=f"{help_dict['slash']}", inline=False)

	elif arg.lower().startswith('morse'):
		embed.add_field(name='Morse Code', value=f"{help_dict['morse'][0]}\n {help_dict['morse'][1]}", inline=False)
        #embed.add_field(name='Note',value='The Prefix `&?` is only required in servers. All the commands will work without the prefix in the bots DM.',inline=False)
		embed.add_field(name='Slash Commands', value=f"{help_dict['slash']}", inline=False)

	elif arg.lower().startswith('tap'):
		embed.add_field(name='Tap Code', value=f"{help_dict['tap'][0]}\n {help_dict['tap'][1]}", inline=False)
        #embed.add_field(name='Note',value='The Prefix `&?` is only required in servers. All the commands will work without the prefix in the bots DM.',inline=False)
		embed.add_field(name='Slash Commands', value=f"{help_dict['slash']}", inline=False)

	elif arg.lower().startswith('bacon'):
		embed.add_field(name='Bacon Cipher', value=f"{help_dict['bacon'][0]}\n {help_dict['bacon'][1]}", inline=False)
        #embed.add_field(name='Note',value='The Prefix `&?` is only required in servers. All the commands will work without the prefix in the bots DM.',inline=False)
		embed.add_field(name='Slash Commands', value=f"{help_dict['slash']}", inline=False)

	else:
		embed.add_field(name="Error the command that you entered could not be found", value="[You can type `&?help` to see a list of all commands](https://bit.ly/2PbNIbf)")

	return embed


async def errormsg(msg, error):
    messages = await msg.channel.history(limit=2).flatten()
    embed=discord.Embed(title="Some Unknown Error Occured", description=f"The command that you tried (`{messages[0].content}`) encountered an error.", color=0xff0000)
    embed.set_author(name="Re-Dcrypt", icon_url="https://i.imgur.com/ynad6vI.png")
    embed.add_field(name='Error for all those nerdy kids out there', value=f'```{error}```')
    
    if msg.guild != None:
        embed.add_field(name="Want to submit this bug to the developer?", value="React to this message with ❗ within the next 10 seconds to send this bug to the developer.", inline=False)
    else:
        embed.add_field(name="Want to submit this bug to the developer?", value="Respond with `!report` within the next 10 seconds to send this bug to the developer.", inline=False)
    
    to_react = await msg.channel.send(embed=embed)

    if msg.guild == None:
        pass
    else:
        await to_react.add_reaction('❗')
    
    def checkg(reaction, user):
        return user == msg.author and str(reaction.emoji) == '❗'
    
    def check(m):
        return m.content.lower() == '!report' and m.channel == msg.channel

    try:
        if msg.guild == None:
            msgi = await bot.wait_for('message', timeout=10., check=check)
        else:
            reaction, user = await bot.wait_for('reaction_add', timeout=10.0, check=checkg)
    except asyncio.TimeoutError:
        pass
    else:
        embed=discord.Embed(title="Bug Report", color=0xff0000)
        embed.set_author(name=msg.author, icon_url=msg.author.avatar_url)
        embed.add_field(name="Command:", value=f"{messages[0].content}", inline=False)
        embed.add_field(name="Error Details: ", value=f'```{error}```')
        bchannel=bot.get_channel(819587658169843782)
        await bchannel.send(embed=embed)
        await msg.channel.send(f"```Bug reported to the developer```")








def command_prefix(bot, message):
    if message.guild is None:
        return ''
    else:
        return '&?'


async def get_prefix(ctx):
  return '' if ctx.guild is None else '&?'

bot = commands.Bot(command_prefix)
slash = SlashCommand(bot, sync_commands=True)
bot.remove_command('help') # default help command SUCKS







@bot.event
async def on_ready():   
  print(f'Logged in as {bot.user}!')
  activity = discord.Game(name=f"&?help | on {len(bot.guilds)} servers")
  await bot.change_presence(activity=activity)

@bot.event
async def on_guild_join(self):
	activity = discord.Game(name=f"&?help | on {len(bot.guilds)} servers")
	await bot.change_presence(activity=activity)
  
@bot.event
async def on_guild_remove(self):
	activity = discord.Game(name=f"&?help | on {len(bot.guilds)} servers")
	await bot.change_presence(activity=activity)
  


@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    if ctx.guild != None:
      await ctx.message.add_reaction('<a:blobthink:821039137037090818>')

  
  else:
			await errormsg(ctx, error)




@bot.command()
async def help(ctx,*,arg: typing.Optional[str] = None):
    await ctx.send(embed=helpcmd(arg))



@bot.command()
async def invite(ctx):
  await ctx.send('https://discord.com/api/oauth2/authorize?client_id=775629409494630410&permissions=67451968&scope=bot')

@bot.command()
async def feedback(ctx,*, cont):
  channel=bot.get_channel(810404758706716672)
  embed=discord.Embed(title="New Feedback", description=cont, color=0x39ff14)
  embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
  mess = await channel.send(embed=embed)
  emoji1='\N{THUMBS UP SIGN}'
  emoji2='\N{THUMBS DOWN SIGN}'
  await mess.add_reaction(emoji1)
  await mess.add_reaction(emoji2)
  #await channel.send(f'{message.author} sent a feedback: {cont}')
  await ctx.send('Feedback sent')


#guild_ids=[769828955023736854]

	

print('Loading basic cogs...')
bot.load_extension("cogs.basic")

print('Loading cipher cogs...')
bot.load_extension("cogs.cipher")

print('Loading other cogs...')
bot.load_extension("cogs.others")

print('Loading slash commands...')
bot.load_extension("cogs.slash")

print('Firing up the Flux Capacitors...')
bot.run(os.getenv('TOKEN'))
