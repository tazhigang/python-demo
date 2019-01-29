# -*- coding: UTF-8 -*-
num1=10
num2=20
num3=30
# total = num1 + num2 + num3; #第一种方式
total = num1 +\
        num2 +\
        num3 #第二种方式 必须有 \ 但是如果有[]或者{}来修饰的不需要 \
print total
print unicode("........变量赋值及数据类型............", encoding='utf-8')
# 变量赋值及数据类型
count=52 #整型类型
miles=20.1  #浮点类型
name="John" #字符串类型
print count
print miles
print name
print unicode("........多个变量赋值............", encoding='utf-8')
#多个变量赋值
a=b=c=d=1
print a
print b
print c
print d
print unicode("........多个变量赋值2............", encoding='utf-8')
a,b,c = 1 ,2.0,"zhangdan";
print a
print b
print c
'''
    python中有5个标准数据类型
        1.Number        数字
        2.String        字符串
        3.List          列表
        4.Tuple         元组
        5.Dictionary    字典
'''