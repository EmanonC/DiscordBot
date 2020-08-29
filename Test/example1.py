import discord
# from  import token
from pipicheck import PiPiChecker
from pipiTimmer import *

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    for channal in client.get_all_channels():
        print(channal.name,channal.id)
        # print (channal.type)
    print("=========")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('hello my friend')

    content=message.content
    checker=PiPiChecker()
    if checker.checkContent(content):
        await message.channel.send(PiPiTimmer().getTime(datetime.datetime.now()))

    if message.content.startswith('play'):
        user=message.author
        print(user.id)
        print(client.get_user(user.id).name)
        for channal in client.get_all_channels():
            if channal.type==discord.ChannelType.voice:
                print(channal.name)
                for member in channal.members:
                    print(member.name)
                    if (member.name==user.name):
                        print(channal.name)
                        print(channal.id)
                        vc=client.get_channel(channal.id)
                        print("dsfg",vc)
                        voiceClient= await  vc.connect()
                        voiceClient.play(discord.FFmpegPCMAudio('/Users/yilunhuang/Desktop/成都.mp3'))

def readFile(filename):
    filehandle = open(filename)
    S= (filehandle.read())
    filehandle.close()
    return S

filename = "../Config/token"
tokenS=readFile(filename)

client.run(tokenS)