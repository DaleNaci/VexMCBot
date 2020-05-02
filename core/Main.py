import asyncio

import discord
from discord.ext.commands import Bot
from discord.ext import commands

from MinecraftServer import MinecraftServer


Client = discord.Client()
bot = commands.Bot(command_prefix = "!")

bot.remove_command("help")

serverTU = MinecraftServer("Vextossup.join-mc.net")
serverTT = MinecraftServer("51.161.120.109:25616")
serverNE = MinecraftServer("sackattack.join-game.net")
serverSURV = MinecraftServer("144.217.103.86:25586")


def format_response(response):
    count = response[0]
    players = response[1]

    if count == 0:
        reply = "0 players."
    elif count == 1:
        reply = "{} player:```\n{}\n```".format(str(count), "\n".join(players))
    else:
        reply = "{} players:```\n{}\n```".format(str(count), "\n".join(players))

    return reply


@bot.event
async def on_ready():
    print("Bot is ready!")


@bot.command()
async def tu(ctx):
    lookup = serverTU.server_lookup()
    response = format_response(lookup)

    await ctx.send(response)


@bot.command()
async def tt(ctx):
    lookup = serverTT.server_lookup()
    response = format_response(lookup)

    await ctx.send(response)


@bot.command()
async def ne(ctx):
    lookup = serverNE.server_lookup()
    response = format_response(lookup)

    await ctx.send(response)


@bot.command()
async def surv(ctx):
    lookup = serverSURV.server_lookup()
    response = format_response(lookup)

    await ctx.send(response)


@bot.command()
async def all(ctx):
    countTU = str(serverTU.player_count())
    countTT = str(serverTT.player_count())
    countNE = str(serverNE.player_count())
    countSURV = str(serverSURV.player_count())

    reply = (
        "```\n"
        "Toss Up:           " + countTU + " players\n"
        "Tower Takeover:    " + countTT + " players\n"
        "Nether Survival:   " + countNE + " players\n"
        "Survival:          " + countSURV + " players\n"
        "```"
    )

    await ctx.send(reply)


@bot.command()
async def help(ctx):
    reply = (
        "```\n"
        "!tu    Toss Up\n"
        "!tt    Tower Takeover\n"
        "!ne    Nether Survival\n"
        "!surv  Survival\n"
        "!all   All Servers\n"
        "```"
    )

    await ctx.send(reply)


with open("token.txt", "r") as f:
    lines = f.readlines()
    token = lines[0].strip()

bot.run(token)
