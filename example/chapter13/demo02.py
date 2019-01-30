# -*- coding: UTF-8 -*-
'''
    以下是调用函数时可使用的正式参数类型：
    必备参数 
    关键字参数
    默认参数
    不定长参数
'''
def printName(str):
    print str;

printName(str = "my String") #关键字参数，顺序不影响

def printMsg(name,age=22): #默认参数
    print name;
    print age;
    return;

printMsg("wiki",25)
printMsg("wiki")
#可变长参数
def add(a,*b):
    sum=0;
    sum+=a;
    for i in b:
        sum+=i;
    print sum;
    return sum;

add(1)

add(1,2,3,4,5,6,7)