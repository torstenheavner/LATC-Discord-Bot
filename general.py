import random
from importlib import *

from discord.ext import commands

import useful as u


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = "MAGENTA"
        self.name = "GENERAL"

    def cog_unload(self):
        u.print(self.color, self.name, "OFFLINE")

    @commands.command(brief="Check if the bot is online")
    async def ping(self, ctx):
        await ctx.send("Pong! The bot is online.")
        u.cprint(self.color, self.name, ctx, "BOT PINGED")

    @commands.command(brief="Call someone cringe")
    async def cringe(self, ctx):
        await ctx.delete()
        await ctx.send(random.choice(["that was cringe,,,,", "cringe.", "stop,, dont do that ever again", "that was so cringe", "i can confirm that this is cringe", "you are big cringe", "uh oh, big cringe", "you are unlike the fred movie trilogy,\nwhich is to say, you are cringe."]))
        u.cprint(self.color, self.name, ctx, "SOMEONE WAS CRINGE")


def setup(bot):
    u.nprint("MAGENTA", "GENERAL", "ONLINE")
    bot.add_cog(General(bot))
    reload(u)
