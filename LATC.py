import sys

from discord.ext import commands

import useful as u

sys.path.append("T:/all")
bot = commands.Bot(command_prefix=".")

cogs = u.getData()["cogs"]
u.clear()
for extension in cogs:
    bot.load_extension(extension)
    u.nprint("GREEN", "MAIN", "%s INITIALIZED" % extension.upper())


@bot.event
async def on_connect():
    u.nprint("GREEN", "MAIN", "CONNTECTED")


@bot.event
async def on_disconnect():
    u.nprint("GREEN", "MAIN", "DISCONNECTED")


@bot.event
async def on_ready():
    u.nprint("GREEN", "MAIN", "ONLINE")
    u.nprint("GREEN", "MAIN", "ALL PROCESSES INITIALIZED SUCCESFULLY")


@bot.command(brief="Reload all of the bots modules (update the code)")
async def reload(ctx):
    u.cprint("GREEN", "MAIN", ctx, "PROCESSES RE-INITIALIZED")
    log = []
    _cogs = u.getData()["cogs"]
    for _extension in _cogs:
        try:
            bot.reload_extension(_extension)
            u.nprint("GREEN", "MAIN", "%s RE-INITIALIZED" % _extension.upper())
            log.append("\"**%s**\" re-initialized" % _extension)
        except:
            bot.load_extension(_extension)
            u.nprint("GREEN", "MAIN", "%s INITIALIZED" % _extension.upper())
            log.append("\"**%s**\" initialized" % _extension)
    u.nprint("GREEN", "MAIN", "ALL PROCESSES RUNNING")

    await ctx.send("\n".join(log))


with open("T:/all/latc_creds.txt", "r") as token:
    bot.run(token.read())