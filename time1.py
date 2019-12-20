import time
var = time .time()
#print("time of var is since 12:00am ,january 1,1970",var)
#print(time.localtime())
#localtime = time.localtime(time.time())
#print(localtime)


localtime = time.asctime(time.localtime(time.time()))
print("current localtime",localtime)


#getting celender for the month
'''import calendar
var1 = calendar.month(2019,11)
print("Here is the calender :")
print(var1)
''''''
#printing the calender for whole year
import calendar
calendar.prcal(2038)
'''
#unvarified code
'''
import datetime
print(datetime.datetime.now())
#comparision of two date
from datetime import datetime as dt
if(dt.now().year,dt.now().month,dt.now().day,8)
    <dt.now()
    <dt.now().year,dt.now().month,dt.now().day,16):
    print("working hours")
else:
    print("fun time")
'''
