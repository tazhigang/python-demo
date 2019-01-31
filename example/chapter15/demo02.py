# -*- coding: UTF-8 -*-
fo = open("../../file/foo.txt", "w")
print unicode("文件名: ",encoding="utf-8"), fo.name
print unicode("是否已关闭 : ",encoding="utf-8"), fo.closed
print unicode("访问模式 : ",encoding="utf-8"), fo.mode
print unicode("末尾是否强制加空格 : ",encoding="utf-8"), fo.softspace