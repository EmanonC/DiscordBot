import datetime
import math
import random
class PiPiTimmer:
    leaveTime=datetime.datetime(2020,8,29,16)
    def getTime(self,dateNow):
        timeDelta=dateNow-self.leaveTime
        # timeDelta=datetime.timedelta(self.leaveTime, datetime.datetime.now())
        hasLeave=True
        back=""
        if (timeDelta.days<0):
            hasLeave=False
        if (not hasLeave):
            timeDelta=-timeDelta
            hour=math.floor(timeDelta.seconds/60/60)
            mins=math.floor((timeDelta.seconds-hour*60*60)/60)
            sec=timeDelta.seconds-mins*60-hour*60*60
            back=f"皮皮虾还有{hour}小时{mins}分钟{sec}秒就要离开我们了，让我们永远记住他"
            back=self.formatBeforeLeaveBack(hour,mins,sec)
            print(back)
        else:
            print(timeDelta)
            days=timeDelta.days
            hour = math.floor(timeDelta.seconds / 60 / 60)
            mins = math.floor((timeDelta.seconds - hour * 60 * 60) / 60)
            sec = timeDelta.seconds - mins * 60 - hour * 60 * 60
            back = f"皮皮虾已经离开了{hour}小时{mins}分钟{sec}秒，让我们继续怀念他"
            print(back)
        return back

    def formatBeforeLeaveBack(self,hour,mins,sec):
        pipiNames=["皮皮虾","Felix","皮皮"]
        name=random.choice(pipiNames)
        locations=["多伦多","我们","YYZ"]
        location=random.choice(locations)
        timeS=f"{hour}小时{mins}分钟{sec}秒"
        backs=[f"还有{timeS}{name}就要离开{location}了",
               f"再过{timeS}{name}的航班就要起飞",
               f"距离{name}离开{location}还有{timeS}"
               ]
        return random.choice(backs)

    def getSaoHua(self):
        filehandle = open("goodbyeWords")
        S = (filehandle.readlines())
        filehandle.close()
        return random.choice(S)

p=PiPiTimmer()
# p.getTime(datetime.datetime.now())
p.getTime(datetime.datetime(2020,8,30,16))