import sys
import discord
import random 
from discord import member
from discord import channel
from discord.ext import commands
from discord.message import Message

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '*', intents = intents)

_8ball= [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]

questions= []
bad_words= ["fuck", "shit", "pussy", "cock", "asshole", "bumboclaat", "bomboclaat", "Cum", "cum", "battyman", "fish",
            "faggat", "bowaz", "piss", "pussyhole", "shit face", "shit face", "Where are the girls?", "cocky", "cacky",
            "assface", "rum and raisin", "buff", "faggot", "suck your mada", "yuh mada", "yuh mada suck mi", "suck yuh mada wid a straw",
            "bbc"]
response= ["Please don't answer like an idiot...", "This question is easy...", "Please don't answer like a five year old..."
            "Your answer should make sense", "Give me a paragraph lol. Don't worry, I know you're too dumb to do that..."]

#server_members= ["ShadowNext57#4254", "Artemis_Sama#4250", "daboy#7472", "Cabrini#7637", "GEN_BANZE#2803", "Gough#1419"
#                "justdanny#7457", "Lionspalm101(Revampt)#6819"]

test_members= ["Nobody123#6440", "AllahDalla#3544"]

anime_channel= 846443377624481793
test_channel= 850566296567283735

message_to_dm= "Please to join us in today's stream.\n Hope you're free and ready to watch some anime."

def make_bot_questions():
    f= open("C:\\Users\\Dean-Andrew\\Desktop\\Alscripts\\questions.txt", "r")
    sentence= ""
    while f.readline() not in "*":
        sentence = f.readline().replace("\n", "").replace("*", "")
        questions.append(sentence)

# def make_swear_words():
#     f= open("C:\\Users\\Dean-Andrew\\Desktop\\Alscripts\\SwearWords.txt", "r")
#     sentence= ""
#     while f.readline() not in "*":
#         sentence = f.readline().replace("\n", "").replace("*", "")
#         bad_words.append(sentence)
    #print(bad_words)

make_bot_questions()
#make_swear_words()

@client.event
async def on_ready():
    print("Allah Dalla 5000 is ready...")
    channel= client.get_channel(anime_channel)
    await channel.send("Hello there !! \n I am Anime Bot5000. \n Press '<asterisk sign>help' to see my commands. \n Press '<asterisk sign>talk' to talk to me.")

@client.event
async def on_member_join(member):
    print(f"{member} has joined the server")
    channel= client.get_channel(anime_channel)
    await channel.send(f"{member} has joined.\n Hello, I am Anime Bot5000.\n This is a chill spot where you can relax and talk about anime.\n Please enjoy.\n '*Happy robot noises*'.")

@client.event
async def on_member_remove(member):
    print(f"{member} has left the server")
    channel= client.get_channel(anime_channel)
    await channel.send(f"{member} has left.\n I kinda liked them.\n '*Sad robot noises*'.")

   

@client.command()
async def talk(ctx):
    await ctx.send(f"Question: {random.choice(questions)} \n {random.choice(response)}")


@client.command(aliases=["play","game", "8ball"])
async def game_time(ctx, *question):
    string= question
    sentence= ""
    for x in string:
        sentence += x+" "

    if question.__len__() == 0:
        await ctx.send("Ask a question nigga. How else am I suppose to tell you an answer ...")
    elif question.__len__() > 0 and question.__len__() < 3:
        await ctx.send("This ain't even a proper question. Dummies ....")
    else:
        await ctx.send(f"Question: {sentence} \nAnswer: {random.choice(_8ball)} \n")

@client.command()
async def clear(ctx, passwd= None, amount= 100):
    if passwd == "bot":
        await ctx.channel.purge(limit=amount)
        await ctx.send("Good lord, these moderators don't work hard enough. I cleaned the chat for you.\n You're welcome ...")
    else:
        await ctx.send("You are not authorised. Sucks to be you ...")

@client.event
async def on_message(message : discord.message):
    await client.process_commands(message)
    for words in bad_words:
        if words in message.content:
            await message.channel.purge(limit=1)
            print(f"Message was deleted successfully from {message.author.mention}")
            embed= discord.Embed(title="Profanity Alert!", description= f"{message.author.mention} said ||{words}||", color= discord.Color.blurple())
            await message.channel.send(embed= embed)
            await message.channel.send(f"{message.author.mention}, we don't use those words here.\n Only I can .... beep bop")
            return
    
@client.command()
async def shutdown(ctx, passwd= None, second_passwd= None):
    if passwd == "bot0" and second_passwd == "0bot":
        await ctx.channel.purge(limit=3)
        await ctx.send("Shutting down... \n Good-bye")
        await client.close()
    elif passwd == "bot0" or second_passwd == "0bot":
        await ctx.channel.purge(limit=3)
        await ctx.send("A password is missing my dude.\n Try again... beep bop")
    else:
        await ctx.send("You are not authorised.\n Sucks to be you")


@client.command()
async def private_message(ctx):
    # for p in person:
    #     await p.send(content= "I have arrived in your DM's")
    members= client.get_all_members()
    for x in members:
        await x.send(content= message_to_dm)
        print(f"Message: {message_to_dm}.\n Sent to: {x.name}")
        continue
        

    #await members.send(content="Hello, did I make it to your dm?")
        
    
    


# def test(yessir, *args):
#     if args.__len__() > 1:
#         print("It's greater than one")
#         print(f"This is the good message: {yessir}")
#     else:
#         print("Failed")

# test("Thank-you Jesus")        
client.run('ODQ5ODgzMzU3MjkzODM4Mzk2.YLhpjg.WZmC8dtnJJ1jjOaWHyCnR7bBgXI')