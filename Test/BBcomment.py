import datetime
class BBcomment:
    def load(self,index,userID,userName,context,datetime1):
        self.index=index
        self.userID=userID
        self.userName=userName
        self.context=context
        self.datetime=datetime.datetime.strptime(datetime1,"%Y-%m-%d %H:%M:%S.%f")

    def makeComment(self,index,userID,userName,context):
        self.index = index
        self.userID = userID
        self.userName = userName
        self.context = context
        self.datetime=datetime.datetime.now()

    def readComment(self):
        dt=self.datetime
        return f"{self.userName}在{dt.month}月{dt.day}日 {dt.hour}:{dt.minute} 对皮皮虾说：{self.context}"

