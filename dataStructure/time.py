# author: HR
# date: 2018/2/9

import time,datetime

localTime = time.localtime(time.time())

print("LocalTime:", localTime)

# 日期格式转换
print("dateTime now:", time.strftime('%Y/%m/%d %H:%M:%S'))

print("dateTime now:", str(datetime.datetime.now())[:19])

expire_time = "2018-02-09 15:01:19"

d = datetime.datetime.strptime(expire_time, "%Y-%m-%d %H:%M:%S")
print(d)

# 日期运算
today = datetime.date.today()
print("Today:", today)

delayDays = datetime.timedelta(days=2)
print("前天：", today - delayDays)
print("后天：", today + delayDays)

delaySeconds = datetime.timedelta(seconds=10)
delayMinutes = datetime.timedelta(minutes=10)
delayHours = datetime.timedelta(hours=1)

print("Day:", delayDays, "Hour:", delayHours, "Minutes:", delayMinutes, "Seconds:", delaySeconds)

# 日期格式转化为秒
d = datetime.date.today()
print(time.mktime(d.timetuple()))
