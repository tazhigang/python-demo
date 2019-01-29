# -*- coding: UTF-8 -*-
'''
    数字类型有4中类型
    1.int       有符号整型
    2.long      长整型[也可以代表八进制和十六进制]
    3.float     浮点型
    4.complex   复数
    注意：long 类型只存在于 Python2.X 版本中，
         在 2.2 以后的版本中，int 类型数据溢出
         后会自动转为long类型。在 Python3.X版
         本中 long 类型被移除，使用 int 替代。
'''
str="adbcdefg"
print str[1:5]
print str*2
hello="hello "
world="world"
print hello+world
'''
    List（列表） 是 Python 中使用最频繁的数据类型。
    列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。
    列表用 [ ] 标识，是 python 最通用的复合数据类型。
'''
names=["John","Tom","张三"]
print names
print names[0]