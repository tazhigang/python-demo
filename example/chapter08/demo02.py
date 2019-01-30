# -*- coding: UTF-8 -*-
# 条件判断语句
#判断一个数的大小
num = 20
if num <30:
    print  unicode("留级",encoding="utf-8"),num
elif num < 60 and num >=30:
    print unicode("不及格",encoding="utf-8"),num
elif num <=70:
    print  unicode("及格",encoding="utf-8"),num
elif num <=90:
    print  unicode("良好",encoding="utf-8"),num
else:
    print  unicode("优秀",encoding="utf-8"),num