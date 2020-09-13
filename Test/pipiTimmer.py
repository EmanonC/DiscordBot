import datetime
import math
import random
class PiPiTimmer:
    #出发时间
    leaveTime=datetime.datetime(2020,8,29,16,41)
    #到达上海时间
    arriveSHTime=datetime.datetime(2020,8,30,6,2)
    #离开上海时间
    leaveSHTime=datetime.datetime(2020,9,6,0,0)
    #结束隔离时间
    endQuarantineTime=datetime.datetime(2020,9,12,21,0)



    locations=["多伦多","我们","YYZ"]
    pipiNames = ["皮皮虾", "Felix", "皮皮"]

    def getTime(self,dateNow):
        timeDelta=dateNow-self.leaveTime
        # timeDelta=datetime.timedelta(self.leaveTime, datetime.datetime.now())
        hasLeave=True
        back=""
        if (timeDelta.days<0):
            hasLeave=False

        if (not hasLeave):
            #没有出发的话，返回倒计时
            timeDelta=-timeDelta
            hour=math.floor(timeDelta.seconds/60/60)
            mins=math.floor((timeDelta.seconds-hour*60*60)/60)
            sec=timeDelta.seconds-mins*60-hour*60*60
            back=f"皮皮虾还有{hour}小时{mins}分钟{sec}秒就要离开我们了，让我们永远记住他"
            back=self.formatBeforeLeaveBack(hour,mins,sec)
            print(back)
            #已经出发了，返回计时器
        else:
            # days=timeDelta.days
            # hour = math.floor(timeDelta.seconds / 60 / 60)
            # mins = math.floor((timeDelta.seconds - hour * 60 * 60) / 60)
            # sec = timeDelta.seconds - mins * 60 - hour * 60 * 60
            # back = f"皮皮虾已经离开了{hour}小时{mins}分钟{sec}秒，让我们继续怀念他"
            back=self.formatAfterLeaveBack()
            # print(back)
        return back

    #如果还没有出发，返回一个倒计时
    def formatBeforeLeaveBack(self,hours,mins,sec):
        #人名
        name=random.choice(self.pipiNames)
        #地点
        location=random.choice(self.locations)
        #时间
        timeS=f"{hours}小时{mins}分钟{sec}秒"
        #返回倒计时格式
        backs=[f"还有{timeS}{name}就要离开{location}了",
               f"再过{timeS}{name}的航班就要起飞",
               f"距离{name}离开{location}还有{timeS}"
               ]
        return random.choice(backs)

    def formatAfterLeaveBack(self):
        # 人名
        name = random.choice(self.pipiNames)
        # 地点
        location = random.choice(self.locations)

        # 时间
        fromLeaveToronto=datetime.datetime.now()-self.leaveTime
        # 返回倒计时格式
        timeS=self.getHourMins(fromLeaveToronto)
        backs = [
            # f"{name}的飞机已经起飞{timeS}了",
                 # f"从{location}前往上海的飞机已经出发{timeS}了",
                 f"{name}离开{location}已经{timeS}了",
                 f"{name}离开{location}的第{timeS}，想他",
                 f"距离我们和{name}告别已经{timeS}了"
                 ]

        fromArriveSH=datetime.datetime.now()-self.arriveSHTime
        timeS = self.getHourMins(fromArriveSH)
        # backs.append(f"{name}已经在上海吃吃喝喝{timeS}了")
        backs.append(f"{name}已经抵达上海{timeS}了")

        # fromLeaveSH=datetime.datetime.now()-self.leaveSHTime
        # if (fromLeaveSH.days<0):
        #     fromLeaveSH =  self.leaveSHTime-datetime.datetime.now()
        #     timeS = self.getHourMins(fromLeaveSH)
            # backs.append(f"{name}还有{timeS}就要前往嘉兴了")
            # backs.append(f"{name}在上海吃吃喝喝睡睡的日子还有{timeS}")


        fromEndQuarantine=datetime.datetime.now()-self.endQuarantineTime
        if (fromEndQuarantine.days<0):
            fromEndQuarantine =  self.endQuarantineTime-datetime.datetime.now()
            timeS = self.getHourMins(fromEndQuarantine)
            backs.append(f"{name}还有{timeS}就要结束隔离了")
            backs.append(f"再过{timeS},{name}就会浪变全中国")
        else:
            fromEndQuarantine = datetime.datetime.now()-self.endQuarantineTime
            timeS = self.getHourMins(fromEndQuarantine)
            backs.append(f"{name}结束隔离{timeS}了，杭州瑟瑟发抖")
            backs.append(f"{name}浪遍全中国的{timeS},为他鼓掌！")
            backs.append(f"{name}已经被释放了{timeS},猜猜他都干了些啥？")

        return random.choice(backs)

    #从goodbyeWords中选出一句骚话
    def getSaoHua(self):
        filehandle = open("goodbyeWords", encoding="utf8")
        S = (filehandle.readlines())
        filehandle.close()
        words=random.choice(S)
        words =words.replace("your","PiPiXia's")
        words=words.replace("you","PiPiXia")
        words =words.replace("你","皮皮虾")
        return words

    def getWYY(self):
        filehandle = open("wangyiyun", encoding="utf8")
        S = (filehandle.readlines())
        filehandle.close()
        words = random.choice(S)
        words = words.replace("your", "PiPiXia's")
        words = words.replace("you", "PiPiXia")
        words = words.replace("我", "皮皮虾")
        return words

    def getHourMins(self,timedelta):
        days=timedelta.days
        hours = math.floor(timedelta.seconds / 60 / 60)
        mins = math.floor((timedelta.seconds - hours * 60 * 60) / 60)
        sec = timedelta.seconds - mins * 60 - hours * 60 * 60
        if (days>0):
            timeS=f"{days}天{hours}小时{mins}分钟"
        else:
            if (hours>0):
                timeS = f"{hours}小时{mins}分钟{sec}秒"
            else:
                timeS = f"{mins}分钟{sec}秒"
        return timeS

    def getNextMealTime(self):
        dt=datetime.datetime.now()
        dt=dt+datetime.timedelta(hours=12)
        year=dt.year
        month=dt.month
        day=dt.day

        breakfastTime=datetime.datetime(year,month,day,7,30)
        lunchTime=datetime.datetime(year,month,day,11,30)
        dinnerTime=datetime.datetime(year,month,day,17,30)

        if (dt<breakfastTime):
            td=breakfastTime-dt
            ts=self.getHourMins(td)
            mealName="早饭"
        elif (dt<lunchTime):
            td=lunchTime-dt
            ts = self.getHourMins(td)
            mealName = "午饭"
        elif (dt<dinnerTime):
            td=dinnerTime-dt
            ts = self.getHourMins(td)
            mealName = "晚饭"
        else:
            breakfastTime=breakfastTime+datetime.timedelta(days=1)
            td = breakfastTime - dt
            ts = self.getHourMins(td)
            mealName = "早饭"
        name=random.choice(self.pipiNames)
        back=f"{name}的{mealName}将在{ts}后到达门口。"

        fromEndQuarantine = self.endQuarantineTime - datetime.datetime.now()
        timeS = self.getHourMins(fromEndQuarantine)
        back=f"{name}已经处于无人投食状态{timeS}了 \n希望他能在{ts}后按时吃上{mealName}"
        return back



# p=PiPiTimmer()
# print(p.getNextMealTime())
# print(p.getWYY())