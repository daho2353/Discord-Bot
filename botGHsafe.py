#! python3.6
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get
import asyncio
import time
import random

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

osrsSkills = {
    "combat": "Train your combat stats! Those crabs aren't going to kill themselves",
    "prayer": "Train your prayer! It'll make your life just a bit easier",
    "magic": "Train your magic! I don't care if it sucks ass!",
    "rc": "Train your runecrafting :smirk: ",
    "construction": "Train you construction! Time to make a dream house",
    "agility": "Train your agility, the shortcuts and stamina are worth your time",
    "herblore":  "Train your herblore, potions are good money!",
    "crafting": "Train your crafting, it's so easy a caveman could do it",
    "thieving": "Train your thieving, What if you get the coon!",
    "fletching": "Train your fletching, idk why you would want to do that but you need that 99 somehow",
    "slayer": "Train your slayer, that task isn't going to finish itself!",
    "hunter": "Train your hunter, it'll be worth it down the road",
    "mining": "Train your mining, it's a hassle but you'll be glad you got it done",
    "smithing":  "Train your smithing, just do it!",
    "cooking": "Train your cooking, everyone deserves a cooking break",
    "firemaking": "Train your firemaking, you could get a pheonix pet!",
    "farming": "Train your farming, it's time for an herbrun",
    "woodcutting": "Train your woodcutting, it's a good break from the harder skills",
    "fishing": "Train your fishing, it's a great skill for afking and doing something else",
    "questing": "Might I suggest you go questing?"
 }

ajGame = {
    "love": "I luuuuv aj :blush:",
    "hate": "I hate aj :rage:"
}

errorCode = {
    "italy": "That's not a number... ERROR CODE: ITALY"
}

eightBall = {
    "good1": "That is 100% true!",
    "good2": "I can agree to that",
    "good3": "sounds good to me",
    "good4": "Yes.... definitely",
    "good5": "that's probably true",
    "good6": "lol true",
    "good7": "I mean I guess so",
    "good8": ":thumbsup:",
    "good9": "Si, Oui, Ja, Hai, Yes",
    "good10": "totes magotes dude",
    "neutral1": ":thinking:",
    "neutral2": "that's up to you ",
    "neutral3": "idk what do I look like",
    "neutral4": ":shrug:",
    "neutral5": "possibly",
    "nope1": "no way Jose!",
    "nope2": "naaaaaah",
    "nope3": "lol nope",
    "nope4": "... ok retard",
    "nope5": "not even the slightest chance"
}

    
async def cookie(message): #next step is to make functions for all of the if statements
    await client.send_message(message.channel, ":cookie:")

async def aj(message):
    ajfeel = random.randint(1,2)
    if ajfeel == 1:
        await client.send_message(message.channel, ajGame['love'])
    if ajfeel == 2:
        await client.send_message(message.channel, ajGame['hate'])

async def rando(message):
    await client.send_message(message.channel, "Enter Lower Bound:")
    lowerBound = await client.wait_for_message(author=message.author)
    try:
        lowerBound = int(lowerBound.content)
    except ValueError:
        await client.send_message(message.channel, errorCode['italy'])
        return
    await client.send_message(message.channel, "Enter Upper Bound:")
    upperBound = await client.wait_for_message(author=message.author)
    try:
        upperBound = int(upperBound.content)
    except ValueError:
        await client.send_message(message.channel, errorCode['italy'])
        return
    magic = random.randint(lowerBound, upperBound)
    await client.send_message(message.channel, magic)

async def game(message):
    magic = random.randint(1,10)
    await client.send_message(message.channel, "Guess a number between 1 and 10")
    async def guessf():
        def check(msg):
            return msg in [*range(1,11)]
        message2 = await client.wait_for_message(author=message.author, check=check(message.content))
        try:
            guess = int(message2.content)
        except ValueError:
            await client.send_message(message.channel, errorCode['italy'])
            return
        if guess == magic:
            await client.send_message(message.channel, "You Win!")
        else:
            if guess > magic:
                await client.send_message(message.channel, "too high")      
                await guessf()
            else:
                await client.send_message(message.channel, "too low")
                await guessf()
        await guessf()

async def vote(message):
    updoot = get(client.get_all_emojis(), name='updoot')
    downdoot = get(client.get_all_emojis(), name="downdoot")
    await client.add_reaction(message, emoji = updoot)
    await client.add_reaction(message, emoji = downdoot)

async def atShinoa(message):
    await client.send_message(message.channel, "Baka!")

async def joq(message):
    num = random.randint(1,5)
    i = 0
    while i < num:
        joq = await client.send_message(message.channel, "<@165985005200211969>")
        i +=1
        await client.delete_message(joq)
    await client.delete_message(message)

async def someone(message):
    someone = open("someone.txt", "r")
    namelist = someone.readlines()
    num = random.randint(0,9)
    await client.send_message(message.channel, "<@{}>".format(namelist[num].strip()))

async def skill(message):
    magic = random.randint(1,20)
    if magic == 1:
        await client.send_message(message.channel, osrsSkills['combat'])
    elif magic == 2:
        await client.send_message(message.channel, osrsSkills['prayer'])
    elif magic == 3:
        await client.send_message(message.channel, osrsSkills['magic'])
    elif magic == 4:
        await client.send_message(message.channel, osrsSkills['rc'])
    elif magic == 5:
        await client.send_message(message.channel, osrsSkills['construction'])
    elif magic == 6:
        await client.send_message(message.channel, osrsSkills['agility'])
    elif magic == 7:
        await client.send_message(message.channel, osrsSkills['herblore'])
    elif magic == 8:
        await client.send_message(message.channel, osrsSkills['crafting'])
    elif magic == 9:
        await client.send_message(message.channel, osrsSkills['thieving'])
    elif magic == 10:
        await client.send_message(message.channel, osrsSkills['fletching'])
    elif magic == 11:
        await client.send_message(message.channel, osrsSkills['slayer'])
    elif magic == 12:
        await client.send_message(message.channel,  osrsSkills['hunter'])
    elif magic == 13:
        await client.send_message(message.channel, osrsSkills['mining'])
    elif magic == 14:
        await client.send_message(message.channel, osrsSkills['smithing'])
    elif magic == 15:
        await client.send_message(message.channel, osrsSkills['cooking'])
    elif magic == 16:
        await client.send_message(message.channel, osrsSkills['firemaking'])
    elif magic == 17:
        await client.send_message(message.channel, osrsSkills['farming'])
    elif magic == 18:
        await client.send_message(message.channel, osrsSkills['woodcutting'])
    elif magic == 19:
        await client.send_message(message.channel, osrsSkills['fishing'])
    elif magic == 20:
        await client.send_message(message.channel, osrsSkills['questing'])

async def functionEightBall(message):
    num = random.randint(1,20)
    if num == 1:
        await client.send_message(message.channel, eightBall['good1'])
    elif num == 2:
        await client.send_message(message.channel, eightBall['good2'])
    elif num == 3:
        await client.send_message(message.channel, eightBall['good3'])
    elif num == 4:
        await client.send_message(message.channel, eightBall['good4'])
    elif num == 5:
        await client.send_message(message.channel, eightBall['good5'])
    elif num == 6:
        await client.send_message(message.channel, eightBall['good6'])
    elif num == 7:
        await client.send_message(message.channel, eightBall['good7'])
    elif num == 8:
        await client.send_message(message.channel, eightBall['good8'])
    elif num == 9:
        await client.send_message(message.channel, eightBall['good9'])
    elif num == 10:
        await client.send_message(message.channel, eightBall['good10'])
    elif num == 11:
        await client.send_message(message.channel, eightBall['neutral1'])
    elif num == 12:
        await client.send_message(message.channel, eightBall['neutral2'])
    elif num == 13:
        await client.send_message(message.channel, eightBall['neutral3'])
    elif num == 14:
        await client.send_message(message.channel, eightBall['neutral4'])
    elif num == 15:
        await client.send_message(message.channel, eightBall['neutral5'])
    elif num == 16:
        await client.send_message(message.channel, eightBall['nope1'])
    elif num == 17:
        await client.send_message(message.channel, eightBall['nope2'])
    elif num == 18:
        await client.send_message(message.channel, eightBall['nope3'])
    elif num == 19:
        await client.send_message(message.channel, eightBall['nope4'])
    else:
        await client.send_message(message.channel, eightBall['nope5'])

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    if message.content == "cookie":
        await cookie(message)
    if message.content == "!aj":
        await aj(message)
    if message.content == "!random":
        await rando(message)
    if message.content == "!game":
        await game(message)
    if message.content.startswith("!vote"):
        await vote(message)
    if message.content == "<@558316056314249231>": #do more with this later
        await atShinoa(message)
    #if message.content == "!joq": #leave this out of the !help
    #    await joq(message)
    if message.content == "@someone": #make this pull from all people in a server rather than just our server
        await someone(message)
    if message.content == "!skill":
        await skill(message)
    if message.content.startswith("!8ball"):
        await functionEightBall(message)

