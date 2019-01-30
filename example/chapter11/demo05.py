# -*- coding: UTF-8 -*-
# 字典的应用
dir = {"a":1,"b":2,"c":3}
print dir["a"]

dir = {"a":1,"b":2,"c":3}
dir["a"]=13 #修改字典条目
dir["d"]=4  #添加字典条目
print dir

#删除对应条目
del dir["a"]
print dir
#清空字典
dir.clear()
print dir
#删除字典
# del dir
# print dir
#字典的特性
#1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：
dict={"a":1,"a":2}
print dict
#2）键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行，如下实例：
dict = {"name": 'Zara', 'Age': 7} 
#print "dict['Name']: ", dict[['Name']]   #TypeError: unhashable type: 'list'
print dict

     