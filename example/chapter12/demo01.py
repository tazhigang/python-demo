# -*- coding: UTF-8 -*-
# 日期和时间
import time;

time_zone=time.timezone
print time_zone

tick =time.time() #获取当前的时间戳
print tick

locationtime=time.localtime(time.time())
print locationtime

locationFormDate=time.asctime(locationtime)
print locationFormDate
#将当前的首日期格式化输出
defineDate = time.strftime("%Y-%m-%d %H:%M:%S",locationtime)
print defineDate