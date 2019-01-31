# -*- coding: UTF-8 -*-
# 本章讲解python中的异常
try:
    fileObject=open("file/testfile.txt","w")
    try:
        fileObject.write("借鉴简介军军军")
    finally:
        print unicode("关闭文件对象",encoding="utf-8")
        fileObject.close()
except IOError:
    print unicode("找不到文件",encoding="utf-8")
else:
    print "end"
finally:
    print "finally"