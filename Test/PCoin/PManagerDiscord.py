from PCoin import PManager
from sql import SQLTool
from PCoin.FoodValueCalc import *

class PManagerDiscord():
    def __init__(self):
        self.sqlHelper = SQLTool.sql_helper()

    def updatePCoin(self,id,changeValue,remark,time):
        puser,user=self.sqlHelper.getDiscordUser(discord_id=id)
        self.sqlHelper.updatePCoin(user.id,changeValue=changeValue,remark=remark,time=time)

    def updatePValue(self,id,changeValue,remark,time):
        puser,user=self.sqlHelper.getDiscordUser(discord_id=id)
        self.sqlHelper.updatePValue(user.id,changeValue=changeValue,remark=remark,time=time)

    def insertLog(self,id,action,remark,time):
        puser,user = self.sqlHelper.getDiscordUser(discord_id=id)
        self.sqlHelper.insertPLog(user.id, action=action, remark=remark, time=time)

    def feedPiPi(self,id,foodName,time,remark=""):
        puser,user = self.sqlHelper.getDiscordUser(discord_id=id)

        cost=FoodCalculator().getFoodValue(foodName)
        if user.p_coin>=cost:
            back = f"投食成功！ \n花费皮币{cost}个\n您还有皮币{user.p_coin - cost}个"
            self.updatePCoin(id=id,changeValue=-cost,remark="投食",time=time)
            self.sqlHelper.insertPiFood(uid=user.id,foodName=foodName,time=time)
        else:
            back = f"皮币不足，投食失败 ：/"
        return back

    def eatAllFood(self,time):
        back="皮皮虾这顿的食物有：\n"
        foodDict={}
        nameList=[]
        foods=self.sqlHelper.getUneatFood()
        if len(foods)==0:
            return "皮皮虾这顿没东西吃啦！快来feed他吧！"
        for food in foods:
            self.sqlHelper.updatePiFood(food.id,eat_time=time)
            user=self.sqlHelper.getUser(food.user_id)
            lName=""
            if (user.discord_name!=""):
                lName=user.discord_name
            else:
                lName=user.wechat_name
            if lName not in nameList:
                nameList.append(lName)
            if (food.food_name in foodDict):
                foodDict[food.food_name]+=1
            else:
                foodDict.update({food.food_name:1})
        for foodName,num in foodDict.items():
            back+=f"{foodName}*{num}\n"
        back+="本餐由"
        for name in nameList:
            back+=f"{name} "
        back+="赞助\n"
        back+=f"希望皮皮虾吃饱了!"
        return back