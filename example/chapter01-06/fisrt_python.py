# -*- coding: UTF-8 -*-
name = "张三"
age = 12
print unicode(name, encoding='utf-8')
'''
    解决输出中的中文乱码 
    第一步：设置编码 # -*- coding: UTF-8 -*- 
    第二步：对需要解码的中文字符设置解码方式
'''
print age