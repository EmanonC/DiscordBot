import csv
import pandas as pd
from BBcomment import *
import datetime
import random

class BBoard:
    def __init__(self):
        self.lastSave=datetime.datetime.now()
        self.hasSayHello=False

    def addComment(self,userID,userName,context):
        comment=BBcomment()
        self.index+=1
        comment.makeComment(self.index,userID,userName,context)
        self.comments.append(comment)
        if (datetime.datetime.now()-self.lastSave).min>datetime.timedelta(minutes=1):
            self.saveData()
        if (datetime.datetime.now()-self.lastSave).min>datetime.timedelta(minutes=10):
            self.saveWholeBBoard()
        self.lastSave=datetime.datetime.now()
        if (self.index % 10 ==0):
            self.saveWholeBBoard()

    def saveDataTest(self):
        with open("data/data1.csv", "w", encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["index", "user_id", "user_name","comment","datetime"])

    def saveData(self):
        with open(self.filePath, "w", encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["index", "user_id", "user_name","comment","datetime"])
            writer.writerows(self.getCommentsDataform())

    def saveWholeBBoard(self,filename="data/TSData/"+str(datetime.datetime.now().timestamp())+".csv"):
        print("now save ts data")
        self.saveData()
        with open(filename, "w", encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["index", "user_id", "user_name","comment","datetime"])
            writer.writerows(self.getCommentsDataform())

    def loadData(self,filePath):
        data = pd.read_csv(filePath, encoding='utf-8')
        dataLength=len(data)
        print(data)
        self.filePath=filePath
        self.index=dataLength
        self.comments=[]
        for i in range (dataLength):
            comment=BBcomment()
            comment.load(data.iloc[i]["index"],data.iloc[i]["user_id"],data.iloc[i]["user_name"],data.iloc[i]["comment"],data.iloc[i]["datetime"])
            self.comments.append(comment)
        # print(f"读评论{len(self.comments)}/{self.index}")
        # for i in self.comments:
        #     print(i.readComment())

    def getCommentsDataform(self):
        commentsData=[]
        for comment in self.comments:
            commentsData.append([comment.index,comment.userID,comment.userName,comment.context,comment.datetime])
        return commentsData

    def readAllComments(self):
        commentContexts=[]
        for c in self.comments:
            print(c.readComment())
            commentContexts.append(c.readComment())
        return commentContexts

    def readSomeComments(self,n=1):
        if n>self.index:
            n=self.index
        commentSamples=random.sample(self.comments,n)
        commentContexts = []
        for c in commentSamples:
            print(c.readComment())
            commentContexts.append(c.readComment())
        return commentContexts


# b=BBoard()
# b.saveDataTest()
# b.loadData("data/data1.csv")
# b.saveWholeBBoard()
# b.addComment("1","pp","haha")
# b.addComment("1","p","11haha")
# b.readAllComments()
# b.saveWholeBBoard()