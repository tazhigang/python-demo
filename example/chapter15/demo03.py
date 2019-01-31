# -*- coding: UTF-8 -*-
# 文件的写入writelines
fileObject=open("../../file/foo3.txt","w")
fileObject.writelines(
'''你好;
我是;
Jerry!''')
fileObject.close()