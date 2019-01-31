# -*- coding: UTF-8 -*-
# 本章讲解python中的异常
try:
    fileObject=open("testfile.txt","w")
except BaseException:
    print unicode("找不到文件",encoding="utf-8")
else:
    fileObject.write("1111111")
    fileObject.close()