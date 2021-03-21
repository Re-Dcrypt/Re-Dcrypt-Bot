# -*- coding: utf-8 -*-

from discord.ext import commands
import discord
import time
import string
import typing
import asyncio
import sys; sys.path.append("..") # Recognize /utils as a package 
from utils import *




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
    




def setup(bot):
    bot.add_cog(cipher(bot))

