from sqlalchemy import Column, String, create_engine,INTEGER,DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sql.models import *
from sql.tool import readFile
import datetime

class sql_helper:

    def __init__(self):
        self.db=declarative_base()
        sqlLine = self.readFile("../Config/sqlconfig")
        # sqlLine = self.readFile("../../Config/sqlconfig")
        self.engine = create_engine(sqlLine, encoding='utf-8')
        self.DBSession = sessionmaker(bind=self.engine)
        self.db=self.DBSession()

    def addDiscordUser(self,discord_id,discord_name):
        user=User(discord_name=discord_name,discord_id=discord_id)
        self.db.add(user)
        self.db.commit()

    def addWeChatUser(self,wechat_name):
        user=User(wechat_name=wechat_name)
        self.db.add(user)
        self.db.commit()

    def updatePCoin(self,uid,changeValue,remark,time):
        log=PiCoinLog(user_id=uid,p_coin_change=changeValue,time=time,note=remark)
        self.db.add(log)
        self.db.commit()
        user = self.db.query(User).filter(User.id == uid).all()[0]
        user.p_coin+=changeValue
        self.db.commit()

    def updatePValue(self,uid,changeValue,remark,time):
        log=PiValueLog(user_id=uid,p_value_change=changeValue,time=time,remark=remark)
        self.db.add(log)
        self.db.commit()
        user = self.db.query(User).filter(User.id == uid).all()[0]
        user.p_value+=changeValue
        self.db.commit()

    def insertPLog(self,uid,action,remark,time):
        log=PiLog(user_id=uid,action=action,time=time,remark=remark)
        self.db.add(log)
        self.db.commit()

    def insertPiFood(self,uid,foodName,time,remark=""):
        log=PiFood(user_id=uid,food_name=foodName,time=time,remark=remark,has_eat=0)
        self.db.add(log)
        self.db.commit()

    def updatePiFood(self,foodID,eat_time,remark=""):
        food=self.db.query(PiFood).filter(PiFood.id==foodID).all()[0]
        if remark!="":
            food.remark=remark
        food.eat_time=eat_time
        food.has_eat=1
        self.db.commit()

    def getUneatFood(self):
        foods = self.db.query(PiFood).filter(PiFood.has_eat == 0).all()
        return foods

    def getWeChatUser(self,nickName):
        users = self.db.query(User).filter(User.wechat_name == nickName).all()
        if (len(users) > 0):
            user = users[0]
        else:
            self.addWeChatUser(nickName)
            users = self.db.query(User).filter(User.wechat_name == nickName).all()
            user = users[0]
        return self.phraseUser(user),user

    def getUser(self,uid):
        user = self.db.query(User).filter(User.id==uid).all()[0]
        return user

    def getDiscordUser(self,discord_id):
        users = self.db.query(User).filter(User.discord_id == discord_id).all()
        user = users[0]
        return self.phraseUser(user),user

    def addCommentfromWeChat(self,nickName,content,time):
        users = self.db.query(User).filter(User.wechat_name ==nickName).all()
        if (len(users)>0):
            user=users[0]
        else:
            self.addWeChatUser(nickName)
            users = self.db.query(User).filter(User.wechat_name == nickName).all()
            user = users[0]
        comment=Comments(user_id=user.id,content=content,time=time)
        self.db.add(comment)
        self.db.commit()

    def addCommentfromDiscord(self,discord_id,content,time):
        users = self.db.query(User).filter(User.discord_id ==discord_id).all()
        user=users[0]
        comment=Comments(user_id=user.id,content=content,time=time)
        self.db.add(comment)
        self.db.commit()

    def getAllComments(self):
        comments=self.db.query(Comments).all()
        return [self.phraseComment(comment) for comment in comments]

    def phraseComment(self,comment):
        user_id=comment.user_id
        users = self.db.query(User).filter(User.id == user_id).all()
        user = users[0]
        ctt={
            "discord_id":str(user.discord_id),
            "discord_name":str(user.discord_name),
            "wechat_name" :str(user.wechat_name),
            "wechat_id"   :str(user.wechat_id),
            "comment":str(comment.content),
            "time":comment.time,
            # "time":datetime.datetime.strptime(comment.time, '%Y-%m-%d %H:%M:%S.%f'),
            "pCoin":int(user.p_coin),
            "pValue":int(user.p_value),
        }
        # print(ctt)
        return ctt

    def phraseUser(self,user):
        isDiscordUser=user.discord_id!="None"
        ctt = {
            "discord_id": str(user.discord_id),
            "discord_name": str(user.discord_name),
            "wechat_name": str(user.wechat_name),
            "wechat_id": str(user.wechat_id),
            "pCoin": int(user.p_coin),
            "pValue": int(user.p_value),
            "isDiscordUser": isDiscordUser,
        }
        return ctt

    def readFile(self,filename):
        filehandle = open(filename)
        S = (filehandle.read())
        filehandle.close()
        return S

if __name__ == '__main__':
    helper=sql_helper()
    helper.addDiscordUser("134","xia")
    helper.updatePCoin(1,10,"哈哈",datetime.datetime.now())