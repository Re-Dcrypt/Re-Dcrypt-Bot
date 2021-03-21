# -*- coding: utf-8 -*-

from discord.ext import commands
import discord
import time

class basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """ Pong! """
        before = time.monotonic()
        before_ws = int(round(self.bot.latency * 1000, 1))
        message = await ctx.send("🏓 Pong")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"🏓 WS: {before_ws}ms  |  REST: {int(ping)}ms")

    @commands.command(aliases=['servers', 'statistics'])
    async def stats(self, ctx):
        
        await ctx.send(f"{len(ctx.bot.guilds)}")
       
				

def setup(bot):
    bot.add_cog(basic(bot))

