# -*- coding: UTF-8 -*-
# 文件的读取
fileObject=open("../../file/foo6.txt","r")
while(True):
    str2 = fileObject.readline()
    if len(str2)>1:
        print unicode(str2,encoding="utf-8")
    else: 
        break
fileObject.close()