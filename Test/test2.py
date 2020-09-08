import datetime
# s=str(datetime.datetime.now())
# # print(s)
# print(datetime.datetime.strptime(s,"%Y-%m-%d %H:%M:%S.%f").hour)
# dt=datetime.datetime.strptime(s,"%Y-%m-%d %H:%M:%S.%f")
# print(f"{dt.month}月{dt.day}日 {dt.hour}:{dt.minute}")

a=datetime.datetime(2020,9,1,0)
b=datetime.datetime.now()

dt = datetime.datetime.now()
dt = dt + datetime.timedelta(hours=12)
breakfastTime = dt
lunchTime = dt
dinnerTime = dt

