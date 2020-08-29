import datetime
import math
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
            print(back)
        else:
            hour = math.floor(timeDelta.seconds / 60 / 60)
            mins = math.floor((timeDelta.seconds - hour * 60 * 60) / 60)
            sec = timeDelta.seconds - mins * 60 - hour * 60 * 60
            back = f"皮皮虾已经离开了{hour}小时{mins}分钟{sec}，让我们继续怀念他"
            print(back)
        return back

# p=PiPiTimmer()
# p.getTime(datetime.datetime.now())
# p.getTime(datetime.datetime(2020,8,31))