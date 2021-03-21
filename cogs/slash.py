import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
import string
from discord_slash.utils.manage_commands import create_option, create_choice
import sys; sys.path.append("..") # Recognize /utils as a package 
from utils import *
import typing
#import sys; sys.path.append("..") # Recognize /utils as a package 
from main import *

#pip install -U discord-py-slash-command
# https://discord-py-slash-command.readthedocs.io/en/latest/
class Slash(commands.Cog):
    def __init__(self, bot):
      self.bot = bot
		
		


    @cog_ext.cog_slash(name="Atbash" , description = "Atbash cipher: a -> z , b -> y ...",
    options=[
               create_option(
                 name="text",
                 description="Enter the text to be decoded/encoded using atbash cipher.",
                 option_type=3,
                 required=True
               )
             ])
    async def _atbash(self, ctx: SlashContext, text: str):
      await ctx.send(f"```{atbash(text)}```")
		
    @cog_ext.cog_slash(name="Base64" , description = "Encode/Decodes a base64 encoded string!",
    options=[
               create_option(
                 name="text",
                 description="Base64 String",
                 option_type=3,
                 required=True
               ),
							 create_option(
                 name="mode",
                 description="Decode/Encode",
                 option_type=3,
                 required=True,
								 choices=[
                  create_choice(
                    name="Encode",
                    value="encode"
                  ),
                  create_choice(
                    name="Decode",
                    value="decode"
                  )
                ]
               )
             ])
    async def _base64_decode(self, ctx: SlashContext, text: str , mode: str):
      await ctx.send(f"```{base64(text, mode)}```")
    


    @cog_ext.cog_slash(name="Caesar", description = "Encrypts/Decypts a string with the Caesar Cipher!", options=[
                create_option(
                 name="text",
                 description="Text",
                 option_type=3,
                 required=True
               ),
               create_option(
                 name="key",
                 description="Key",
                 option_type=4,
                 required=False
               )
            ])
    async def _caesar_cipher(self, ctx: SlashContext, text: str, key: typing.Optional[int] = None,):
      await ctx.send(f"```{caesar(text,key)}```")

    @cog_ext.cog_slash(name="Vigenere", description = "Encrypts/Decypts a string with the Vigenere Cipher!", options=[
                create_option(
                 name="Key",
                 description="Key",
                 option_type=3,
                 required=True
               ),
               create_option(
                 name="text",
                 description="text",
                 option_type=3,
                 required=True
               ),
							 create_option(
                 name="mode",
                 description="Decode/Encode",
                 option_type=3,
                 required=True,
								 choices=[
                  create_choice(
                    name="Encode",
                    value="encrypt"
                  ),
                  create_choice(
                    name="Decode",
                    value="decrypt"
                  )
                ]
               )
            ])
    async def _vigenere(self, ctx: SlashContext, text: str, key: str , mode):
      await ctx.send(f"```{vigenere(text,key ,mode )}```")
    
    @cog_ext.cog_slash(name="Reverse", description="Reverses a string. That's literally all this does...", options=[
              create_option(
                name="text",
                description="text",
                option_type=3,
                required=True
              )
    ])
    async def _reverse(self, ctx: SlashContext, text: str):
      await ctx.send(f'```{text[::-1]}```')

    @cog_ext.cog_slash(name="Bacon" , description = "Encode/Decodes a string using bacon cipher",
    options=[
               create_option(
                 name="text",
                 description="text",
                 option_type=3,
                 required=True
               ),
							 create_option(
                 name="mode",
                 description="Decode/Encode",
                 option_type=3,
                 required=True,
								 choices=[
                  create_choice(
                    name="Encode",
                    value="encode"
                  ),
                  create_choice(
                    name="Decode",
                    value="decode"
                  )
                ]
               ),
							 create_option(
                 name="variant",
                 description="Standard/Complete",
                 option_type=3,
                 required=False,
								 choices=[
                  create_choice(
                    name="Standard",
                    value="standard",
                  ),
                  create_choice(
                    name="Complete",
                    value="complete"
                  )
                ]
               )
             ])
    async def _bacon(self, ctx: SlashContext, text: str , mode: str, variant: typing.Optional[str] = "standard"):
      await ctx.send(f"```{bacon_cipher(text.upper(), mode, variant)}```")    
    
    
    @cog_ext.cog_slash(name="A1Z26", description="Decode/Encode using A1Z26 ciphers", options=[
              create_option(
                name="text",
                description="text",
                option_type=3,
                required=True
              )
    ])
    async def _a1z26(self, ctx: SlashContext, text: str):
      await ctx.send(f'```{a1z26(text.split())}```')

    @cog_ext.cog_slash(name="Morse", description="Decode/Encode using Morse code", options=[
              create_option(
                name="text",
                description="text",
                option_type=3,
                required=True
              )
    ])
    async def _morse(self, ctx: SlashContext, text: str):
      await ctx.send(f'```{morse(text)}```')

    @cog_ext.cog_slash(name="Tap", description="Decode/Encode using Tap code", options=[
              create_option(
                name="text",
                description="text",
                option_type=3,
                required=True
              )
    ])
    async def _tap(self, ctx: SlashContext, text: str):
      await ctx.send(f'```{tap(text)}```')

    @cog_ext.cog_slash(name="Null", description="Decode using Null cipher (takes the first letter from each word)", options=[
              create_option(
                name="text",
                description="text",
                option_type=3,
                required=True
              )
    ])
    async def _null(self, ctx: SlashContext, text: str):
      await ctx.send(f'```{null(text)}```')
	
    @cog_ext.cog_slash(name="help" , description = "Re-Dcrypt Bot Help",
    options=[

			create_option(
				name="command",
				description="Specific Command",
				option_type=3,
				required=False,
								choices=[
				create_choice(
				name="Caesar Cipher",
				value="caesar"
				),
				create_choice(
				name="Vigenere Cipher",
				value="vigenere"
				),
				create_choice(
				name="Null Cipher",
				value="null"
				),
				create_choice(
				name="A1Z26 Cipher",
				value="a1z26"
				),
				create_choice(
				name="Base64",
				value="base64"
				),
				create_choice(
				name="Atbash Cipher",
				value="atbash"
				),
				create_choice(
				name="Morse Code",
				value="morse"
				),
				create_choice(
				name="Tap Code",
				value="tap"
				),
				create_choice(
				name="Bacon Cipher",
				value="bacon"
				)
			]
			)
			])
    async def _help(self, ctx: SlashContext, command: typing.Optional[str] = None):
      await ctx.send(embed=helpcmd(command))

def setup(bot):
    bot.add_cog(Slash(bot))