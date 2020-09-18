from pipicheck import PiPiChecker
from pipiTimmer import *
from BulletinBoard import *
from PCoin.PManagerDiscord import PManagerDiscord
from PCoin.PManagerWechat import PManagerWechat
import BulletinBoardSQL
import re
import random
from Tools.userChecker import userChecker


class PipiBot:

    def __init__(self,isDiscord):
        self.bboardsql = BulletinBoardSQL.BulletinBoardSQL()
        self.isDiscord=isDiscord
        if self.isDiscord:
            self.pManagerDiscord=PManagerDiscord()
        else:
            self.pManagerWechat=PManagerWechat()

    def reInit(self):
        self.bboardsql = BulletinBoardSQL.BulletinBoardSQL()
        if self.isDiscord:
            self.pManagerDiscord=PManagerDiscord()
        else:
            self.pManagerWechat=PManagerWechat()

    def phraseString(self,s,userName,uid):
        backTexts=[]
        if self.isStartWith("!pipimeal",s):
            pptimmer = PiPiTimmer()
            backTexts.append(pptimmer.getNextMealTime())

        if self.isStartWith("!comment",s):
            content = s
            content = content.replace("!comment", "", 1)
            content = content.strip()
            if self.isDiscord:
                self.pManagerDiscord.updatePCoin(id=uid,changeValue=random.randint(1,10),remark="Comment",time=datetime.datetime.now())
                ref=self.bboardsql.addCommentFromDiscord(uid,content)
            else:
                self.pManagerWechat.updatePCoin(nickName=userName,changeValue=random.randint(1,10),remark="Comment",time=datetime.datetime.now())
                ref=self.bboardsql.addCommentFromWeChat(userName,content)
            backTexts.append(ref)


        if self.isStartWith("!pipiwyy", s):
            pptimmer = PiPiTimmer()
            backTexts.append(pptimmer.getTime(datetime.datetime.now())+"\n"+pptimmer.getWYY())

        if self.isStartWith("!misspipi", s):
            back=""
            back+=PiPiTimmer().getTime(datetime.datetime.now())+"\n"
            back+=PiPiTimmer().getSaoHua()+"\n"
            back+=f"有什么想留言的吗？请以 \"comment+留言\" 格式留言，现在已经有{self.bboardsql.getCommentsN()}条留言了"+"\n"
            back+="ex: !comment 皮皮虾再见！"
            backTexts.append(back)

        if self.isStartWith("!read", s):
            num = re.findall(r"\d+", s)
            if (len(num) > 0):
                num = int(num[0])
            else:
                num = 1

            backTexts.append(self.bboardsql.readSomeComments(num))

        if self.isStartWith("!feed",s):
            foodName=s.split("!feed")[1]
            if (len(foodName)>0):
                if self.isDiscord:
                    ref=self.pManagerDiscord.feedPiPi(id=uid,foodName=foodName,time=datetime.datetime.now())
                else:
                    ref=self.pManagerWechat.feedPiPi(nickName=userName,foodName=foodName,time=datetime.datetime.now())
                backTexts.append(ref)

        if self.isStartWith("!enjoymeal",s):
            if self.isDiscord:
                if(userChecker().checkPiPi(discord_id=uid)):
                    ref=self.pManagerDiscord.eatAllFood(datetime.datetime.now())
                    backTexts.append(ref)
            else:
                if (userChecker().checkPiPi(userName=userName)):
                    ref=self.pManagerWechat.eatAllFood(datetime.datetime.now())
                    backTexts.append(ref)



        return backTexts

    def isStartWith(self,s,text):
        if (len(s)>len(text)):
            return False

        return s==text[:len(s)]

