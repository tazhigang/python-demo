# -*- coding: UTF-8 -*-
# 函数
def printStr(str):
    print str;
    return str;

str = printStr(unicode("你好呀 我要在控制台打印东西",encoding="utf-8"))
print str

#有关传递参数的问题
def add(a,b): #传值不传引用
    a=b
    print "a=",a;
    print "b=",b;
    print a+b;
    return a+b;

a=10
b=20
c = add(a,b)
print c
print "a = ",a
print "b = ",b
#传引用地址
def changeList(li):
    li[0]="aaa";
    li.append("ddd")
    return li;

changeli=["a","b"]
print changeli
changeList(changeli)
print changeli

