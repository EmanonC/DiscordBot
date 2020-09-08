import discord
# from  import token
from pipicheck import PiPiChecker
from pipiTimmer import *
from BulletinBoard import *
import re

client = discord.Client()
bboard=BBoard()
hasSayHello=False

@client.event
async def on_ready():
    bboard.loadData("data/data1.csv")
    hasSayHello = False
    print('We have logged in as {0.user}'.format(client))
    # for u in client.users:
    #     print(u.id," ",u.name)
    # for channal in client.get_all_channels():
    #     print(channal.name,channal.id)
    #     # print (channal.type)
    #
    # print("=========")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('hello my friend')

    if ((str(message.author.id)=="226151279855009792" or client.get_user(message.author.id).name=="Soyoungsonaive") and not bboard.hasSayHello):
        bboard.hasSayHello = True
        await message.channel.send("皮皮虾你好！欢迎回来！")





    content=message.content
    checker=PiPiChecker()
    if checker.checkContent(content):
        if (not message.content.startswith("!")):
            await message.channel.send(PiPiTimmer().getTime(datetime.datetime.now()))
            await message.channel.send(PiPiTimmer().getSaoHua())
            await message.channel.send(f"有什么想留言的吗？请以 \"comment+留言\" 格式留言，现在已经有{bboard.index}条留言了")
            await message.channel.send("ex: !comment 皮皮虾再见！")

    if message.content.startswith("!pipiwyy"):
        pptimmer=PiPiTimmer()
        await message.channel.send(pptimmer.getTime(datetime.datetime.now()))
        await message.channel.send(pptimmer.getWYY())

    if message.content.startswith("!comment"):
        user = message.author
        print(user.id)
        print(client.get_user(user.id).name)
        content = message.content
        content=content.replace("!comment","",1)
        content=content.strip()
        bboard.addComment(user.id,user.name,content)
        await message.channel.send(f"留言成功！现在已经有{bboard.index}条留言了")
        await message.channel.send("想看看别人的留言吗？试试 \"!read 数字\"")
        await message.channel.send("ex: !read 3 会随机朗读3条留言")

    if message.content.startswith("!pipimeal"):
        pptimmer=PiPiTimmer()
        await message.channel.send(pptimmer.getNextMealTime())

    if message.content.startswith("!read"):
        num=re.findall(r"\d+",message.content)
        if (len(num)>0):
            num=int(num[0])
        else:
            num=1

        comments=bboard.readSomeComments(num)
        for comment in comments:
            await message.channel.send(comment)

    if message.content.startswith("!savedata"):
        bboard.saveWholeBBoard()



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