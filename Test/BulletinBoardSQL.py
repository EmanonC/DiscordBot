from BBcomment import *
import datetime
import random
from sql import SQLTool

class BulletinBoardSQL:
    def __init__(self):
        self.sqlHelper = SQLTool.sql_helper()

    def getCommentsN(self):
        comments = self.sqlHelper.getAllComments()
        return len(comments)

    def getAllComments(self):
        comments=self.sqlHelper.getAllComments()
        BBcomments=[]
        for comment in comments:
            if comment["wechat_name"]!="None":
                userName=comment["wechat_name"]
            else:
                userName = comment["discord_name"]
            bbcomment=BBcomment()
            bbcomment.load(0,0,userName,comment["comment"],comment["time"])
            bbcomment.rawData=comment
            BBcomments.append(bbcomment)
        return BBcomments

    def readSomeComments(self,n=1):
        BBcomments=self.getAllComments()
        if n>len(BBcomments):
            n=len(BBcomments)
        commentSamples=random.sample(BBcomments,n)
        commentContexts = []
        for c in commentSamples:
            print(c.readComment())
            commentContexts.append(c.readComment())
        back=""
        for i in commentContexts:
            back+=i+"\n"
        return back

    def addCommentFromWeChat(self,nickName,context):
        currentTime=datetime.datetime.now()
        self.sqlHelper.addCommentfromWeChat(nickName,context,currentTime)
        userCtt=self.sqlHelper.getWeChatUser(nickName)
        back="评论成功!\n"
        back+=f"您目前有皮币{userCtt['pCoin']}个，皮币用处多多哦\n"
        back+=f"试试!read吧"
        return back

    def addCommentFromDiscord(self,discord_id,context):
        currentTime=datetime.datetime.now()
        self.sqlHelper.addCommentfromDiscord(discord_id,context,currentTime)
        userCtt=self.sqlHelper.getDiscordUser(discord_id)
        back="评论成功!\n"
        back+=f"您目前有皮币{userCtt['pCoin']}个，皮币用处多多哦\n"
        back+=f"试试!read吧"

