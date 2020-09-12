import itchat
from pipiBot import PipiBot
import os
import random

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    UID,userName=getUIDandUserName(msg)
    print(msg.text,UID,userName)
    backs=pipiBot.phraseString(msg.text,userName,UID)
    if len(backs)>0:
        return backs[0]
    # return msg.text

# 处理群聊消息
@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def text_reply_group(msg):
    # print(msg)
    # print(msg.ActualNickName)
    UID = msg["FromUserName"]
    userName=msg.ActualNickName
    print(msg.text, UID, userName)
    backs = pipiBot.phraseString(msg.text, userName, UID)
    print(msg.ActualNickName)
    if msg.ActualNickName=="Potter" or msg.ActualNickName=="":
        SendUserName=msg.ToUserName
    else:
        SendUserName = msg.FromUserName
    if isStartWith(msg.text,"!music"):
        print("in music")
        r=itchat.send('一首成都送给你', toUserName=SendUserName)
        r=itchat.send_file('chengdu2.mp3', toUserName=SendUserName)
        print(r)

    if isStartWith(msg.text,"!pipinight"):
        print("in story")
        r=itchat.send('皮皮虾祝你好梦 \n睡前故事准备中', toUserName=SendUserName)
        r=itchat.send_file(getNightStoryFilePath(), toUserName=SendUserName)
        print(r)

    for back in backs:
        itchat.send(back, toUserName=SendUserName)

def getUIDandUserName(msg):
    UID=msg["FromUserName"]
    userName=itchat.search_friends(userName=msg["FromUserName"])["NickName"]
    # print(itchat.search_friends(userName=msg["FromUserName"]))
    return UID,userName

def isStartWith(s,text):
        if (len(s)>len(text)):
            return False
        return s==text[:len(s)]

def getNightStoryFilePath():
    filePath="data/NightStory"
    fileNames=os.listdir(filePath)
    fileName=random.choice(fileNames)
    return filePath+'/'+fileName

pipiBot=PipiBot()
itchat.auto_login()
itchat.run()