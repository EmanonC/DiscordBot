from sqlalchemy import Column, String, create_engine,INTEGER,DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sql.models import *
from sql.tool import readFile
import pandas as pd
import datetime

class sql_transfer:
    def __init__(self):
        self.db=declarative_base()
        sqlLine = readFile("../../Config/sqlconfig")
        self.engine = create_engine(sqlLine, encoding='utf-8', echo=True)
        self.DBSession = sessionmaker(bind=self.engine)
        self.db=self.DBSession()

    def loadDiscordData(self):
        ctt=[]
        filePath = "../data/data1.csv"
        data = pd.read_csv(filePath, encoding='utf-8')
        dataLength = len(data)

        for i in range(dataLength):
            datarow=data.iloc[i]
            row={
                "discord_id":str(data.iloc[i]["user_id"]),
                "user_name":str(data.iloc[i]["user_name"]),
                "comment":str(data.iloc[i]["comment"]),
                "time":datetime.datetime.strptime(data.iloc[i]["datetime"], '%Y-%m-%d %H:%M:%S.%f'),
            }
            print(row)
            ctt.append(row)
        return ctt

    def dumpToDB(self):
        comments=self.loadDiscordData()
        for comment in comments:
            self.addDiscordUser(str(comment["discord_id"]),comment["user_name"])
            self.addCommentfromDiscord(str(comment["discord_id"]),comment["comment"],comment["time"])

    def addDiscordUser(self,discord_id,discord_name):
        users = self.db.query(User).filter(User.discord_id ==discord_id).all()
        if (len(users)==0):
            user=User(discord_name=discord_name,discord_id=discord_id)
            self.db.add(user)
            self.db.commit()

    def addCommentfromDiscord(self,discord_id,content,time):
        print("1")
        users = self.db.query(User).filter(User.discord_id ==discord_id).all()
        user=users[0]
        comment=Comments(user_id=user.id,content=content,time=time)
        self.db.add(comment)
        self.db.commit()

    def getAllComments(self):
        comments=self.db.query(Comments).all()
        for comment in comments:
            print(comment)




transfer=sql_transfer()
# transfer.addDiscordUser("112","pixia")
# transfer.addCommentfromDiscord("112","哈哈",time=datetime.datetime.now())
transfer.dumpToDB()