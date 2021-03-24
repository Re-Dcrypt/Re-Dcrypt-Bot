# -*- coding: utf-8 -*-

from discord.ext import commands
import discord
import time
import string
import re
import typing
import asyncio
import sys; sys.path.append("..") # Recognize /utils as a package 
from utils import *

alphabet = string.ascii_lowercase


class cipher(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def atbash(self, ctx, * , arg=None):
        
        await ctx.send(f"```{atbash(arg)}```")

    @commands.command()
    async def caesar(self, ctx, key: typing.Optional[int] = None,*,  arg):

        await ctx.send(f"```{caesar(arg,key)}```")
				
    @commands.command()
    async def vigenere_decode(self, ctx, key ,*,  arg):

        await ctx.send(f"```{vigenere(arg,key,'decrypt')}```")
		
    @commands.command()
    async def vigenere_encode(self, ctx, key=None ,*,  arg=None):
        await ctx.send(f"```{vigenere(arg,key,'encrypt')}```")
    

    @commands.command()
    async def bacon_encode(self, ctx, variant ,*, arg=''):
        await ctx.send(f'```{bacon_cipher(arg, "encode" , variant)}```')

    @commands.command()
    async def bacon_decode(self, ctx, variant ,*, arg=''):
        await ctx.send(f'```{bacon_cipher(arg, "decode" , variant)}```')

    @commands.command()
    async def a1z26(self, ctx,*arg):
      await ctx.send(f'```{a1z26(arg)}```')

    @commands.command()
    async def null(self, ctx,*,arg):
      await ctx.send(f'```{null(arg)}```')  
    
    @commands.command()
    async def polybius_encrypt(self, ctx,*, arg):
      square = ''
      embed = discord.Embed(title="Polybius Cipher: ", description="Set Alphabet", color=discord.Color(0x39ff14))
      embed.add_field(name=":one:", value="Alphabet Presets")
      embed.add_field(name=":two:", value="Keyword Alphabet")
      embed.add_field(name=":three:", value="Enter your own alphabet")

      msg = await ctx.send(embed=embed)
      
      await msg.add_reaction('1️⃣')
      await msg.add_reaction('2️⃣')
      await msg.add_reaction('3️⃣')

      def checkg(reaction, user):
        return user == ctx.author
      
      def check(m):
        return m.author == ctx.author and m.channel == msg.channel


      reaction, user = await self.bot.wait_for('reaction_add', timeout=20.0, check=checkg)
        

      if str(reaction.emoji) == '1️⃣':
        embed = discord.Embed(title="Polybius Cipher: ", description="Select Alphabet Presets", color=discord.Color(0x39ff14))
        embed.add_field(name=":one:", value="Default Alphabet(Without the \"J\")", inline=False)
        embed.add_field(name=":two:", value="Default Alphabet (Without the \"V\")", inline=False)
        embed.add_field(name=":three:", value="Default Alphabet (Without the \"W\")", inline=False)
        embed.add_field(name=":four:", value="Default Alphabet (Without the \"Q\")", inline=False)
        embed.add_field(name=":five:", value="Default Alphabet (Without the \"Z\")", inline=False)
        msg = await ctx.send(embed=embed)

        await msg.add_reaction('1️⃣')
        await msg.add_reaction('2️⃣')
        await msg.add_reaction('3️⃣')
        await msg.add_reaction('4️⃣')
        await msg.add_reaction('5️⃣')


        reaction, user = await self.bot.wait_for('reaction_add', timeout=20.0, check=checkg)
        if str(reaction.emoji) == '1️⃣': square = alphabet.replace('j', '')
        elif str(reaction.emoji) == '2️⃣': square = alphabet.replace('v', '')
        elif str(reaction.emoji) == '3️⃣': square = alphabet.replace('w', '')
        elif str(reaction.emoji) == '4️⃣': square = alphabet.replace('q', '')
        elif str(reaction.emoji) == '5️⃣': square = alphabet.replace('z', '')

  
      
        await ctx.send(f'✅ Your alphabet is: **{square}**')
    
      elif str(reaction.emoji) == '2️⃣':
        embed = discord.Embed(title="Polybius Cipher:", description="Create an alphabet from a keyword!", color=discord.Color(0x39ff14))
        embed.add_field(name="Example: ", value="If you input \"cipher\", the alphabet will be cipherabdfgklmnoqstuvwxyz.", inline=False)
        embed.add_field(name="Input: ", value="Please type in a keyword.")
        await ctx.send(embed=embed)
        msgi = await self.bot.wait_for('message', timeout=30.0, check=check)
        msgi = msgi.content
        await ctx.send(f'Using key: **{msgi}**')
        
        # clean up the key

        # Check for non alpha characters
        msgi = msgi.lower()
        msgii = re.sub(r'[^A-Za-z]', '', msgi)
        if msgi != msgii:
          await ctx.send(f'⚠ Warning: Your key contains non-alphabet characters. We have removed the non-alphabet characters from the key and the key is now:  ```{msgii}```')
          msgi = msgii


        msgii = "".join(dict.fromkeys(msgi)) # See https://stackoverflow.com/a/9841328/14437456

        if msgi != msgii:
          await ctx.send(f'⚠ Warning: Your key contains duplicate letters. We have removed the duplicate letters from the key and the key is now: ```{msgii}```')
          msgi = msgii
        
        

        square = msgi
        square = square.replace('j', '')

        for char in alphabet:
          if char not in square and char != 'j':
            square += char
        
        await ctx.send(f'✅ Your alphabet is: **{square}**')
    
      elif str(reaction.emoji) == '3️⃣':
        embed = discord.Embed(title="Polybius Cipher: ", description="Create your own alphabet!", color=discord.Color(0x39ff14))
        embed.add_field(name="Feel like the alphabet presets are too dull? Don't want to create an alphabet from a keyword? Well this section is for you!", value="Enter your own custom made brand new shiny alphabet here!", inline=False)
        embed.add_field(name="Requirements: ", value="Your alphabet must be excatly 25 characters long, not contain any duplicate characters, and contain only alphabet characters.", inline=False)
        await ctx.send(embed=embed)

        msgi = await self.bot.wait_for('message', timeout=60.0, check=check)
        msgi = msgi.content
        await ctx.send(f'Using Alphabet: **{msgi}**')

        msgi = msgi.lower()
        

        msgii = re.sub(r'[^A-Za-z]', '', msgi)
        if msgi != msgii:
          await ctx.send(f'⚠ Warning: Your alphabet contains non-alphabet characters. We have removed the non-alphabet characters from the alphabet and the alphabet is now:  ```{msgii}```')
          msgi = msgii
        

        msgii = "".join(dict.fromkeys(msgi)) # See https://stackoverflow.com/a/9841328/14437456

        if msgi != msgii:
          await ctx.send(f'⚠ Warning: Your alphabet contains duplicate letters. We have removed the duplicate letters from the alphabet and the alphabet is now: ```{msgii}```')
          msgi = msgii
        
        if len(msgi) != 25:
          return await ctx.send(f'❌ Error: Your alphabet is not 25 characters long! Aborting...')
        
        square = msgi



      await ctx.send(f'```{polybius_encrypt(arg, square)}```')

      
    @commands.command()
    async def polybius_decrypt(self, ctx,*, arg):
      square = ''
      embed = discord.Embed(title="Polybius Cipher: ", description="Set Alphabet", color=discord.Color(0x39ff14))
      embed.add_field(name=":one:", value="Alphabet Presets")
      embed.add_field(name=":two:", value="Keyword Alphabet")
      embed.add_field(name=":three:", value="Enter your own alphabet")

      msg = await ctx.send(embed=embed)
      
      await msg.add_reaction('1️⃣')
      await msg.add_reaction('2️⃣')
      await msg.add_reaction('3️⃣')

      def checkg(reaction, user):
        return user == ctx.author
      
      def check(m):
        return m.author == ctx.author and m.channel == msg.channel


      reaction, user = await self.bot.wait_for('reaction_add', timeout=20.0, check=checkg)
        

      if str(reaction.emoji) == '1️⃣':
        embed = discord.Embed(title="Polybius Cipher: ", description="Select Alphabet Presets", color=discord.Color(0x39ff14))
        embed.add_field(name=":one:", value="Default Alphabet(Without the \"J\")", inline=False)
        embed.add_field(name=":two:", value="Default Alphabet (Without the \"V\")", inline=False)
        embed.add_field(name=":three:", value="Default Alphabet (Without the \"W\")", inline=False)
        embed.add_field(name=":four:", value="Default Alphabet (Without the \"Q\")", inline=False)
        embed.add_field(name=":five:", value="Default Alphabet (Without the \"Z\")", inline=False)
        msg = await ctx.send(embed=embed)

        await msg.add_reaction('1️⃣')
        await msg.add_reaction('2️⃣')
        await msg.add_reaction('3️⃣')
        await msg.add_reaction('4️⃣')
        await msg.add_reaction('5️⃣')


        reaction, user = await self.bot.wait_for('reaction_add', timeout=20.0, check=checkg)
        if str(reaction.emoji) == '1️⃣': square = alphabet.replace('j', '')
        elif str(reaction.emoji) == '2️⃣': square = alphabet.replace('v', '')
        elif str(reaction.emoji) == '3️⃣': square = alphabet.replace('w', '')
        elif str(reaction.emoji) == '4️⃣': square = alphabet.replace('q', '')
        elif str(reaction.emoji) == '5️⃣': square = alphabet.replace('z', '')

  
      
        await ctx.send(f'✅ Your alphabet is: **{square}**')
    
      elif str(reaction.emoji) == '2️⃣':
        embed = discord.Embed(title="Polybius Cipher:", description="Create an alphabet from a keyword!", color=discord.Color(0x39ff14))
        embed.add_field(name="Example: ", value="If you input \"cipher\", the alphabet will be cipherabdfgklmnoqstuvwxyz.", inline=False)
        embed.add_field(name="Input: ", value="Please type in a keyword.")
        await ctx.send(embed=embed)
        msgi = await self.bot.wait_for('message', timeout=30.0, check=check)
        msgi = msgi.content
        await ctx.send(f'Using key: **{msgi}**')
        
        # clean up the key

        # Check for non alpha characters
        msgi = msgi.lower()
        msgii = re.sub(r'[^A-Za-z]', '', msgi)
        if msgi != msgii:
          await ctx.send(f'⚠ Warning: Your key contains non-alphabet characters. We have removed the non-alphabet characters from the key and the key is now:  ```{msgii}```')
          msgi = msgii


        msgii = "".join(dict.fromkeys(msgi)) # See https://stackoverflow.com/a/9841328/14437456

        if msgi != msgii:
          await ctx.send(f'⚠ Warning: Your key contains duplicate letters. We have removed the duplicate letters from the key and the key is now: ```{msgii}```')
          msgi = msgii
        
        

        square = msgi
        square = square.replace('j', '')

        for char in alphabet:
          if char not in square and char != 'j':
            square += char
        
        await ctx.send(f'✅ Your alphabet is: **{square}**')
    
      elif str(reaction.emoji) == '3️⃣':
        embed = discord.Embed(title="Polybius Cipher: ", description="Create your own alphabet!", color=discord.Color(0x39ff14))
        embed.add_field(name="Feel like the alphabet presets are too dull? Don't want to create an alphabet from a keyword? Well this section is for you!", value="Enter your own custom made brand new shiny alphabet here!", inline=False)
        embed.add_field(name="Requirements: ", value="Your alphabet must be excatly 25 characters long, not contain any duplicate characters, and contain only alphabet characters.", inline=False)
        await ctx.send(embed=embed)

        msgi = await self.bot.wait_for('message', timeout=60.0, check=check)
        msgi = msgi.content
        await ctx.send(f'Using Alphabet: **{msgi}**')

        msgi = msgi.lower()
        

        msgii = re.sub(r'[^A-Za-z]', '', msgi)
        if msgi != msgii:
          await ctx.send(f'⚠ Warning: Your alphabet contains non-alphabet characters. We have removed the non-alphabet characters from the alphabet and the alphabet is now:  ```{msgii}```')
          msgi = msgii
        

        msgii = "".join(dict.fromkeys(msgi)) # See https://stackoverflow.com/a/9841328/14437456

        if msgi != msgii:
          await ctx.send(f'⚠ Warning: Your alphabet contains duplicate letters. We have removed the duplicate letters from the alphabet and the alphabet is now: ```{msgii}```')
          msgi = msgii
        
        if len(msgi) != 25:
          return await ctx.send(f'❌ Error: Your alphabet is not 25 characters long! Aborting...')
        
        square = msgi
      await ctx.send(f'```{polybius_decrypt(arg, square)}```')

def setup(bot):
    bot.add_cog(cipher(bot))

