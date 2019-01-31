# -*- coding: UTF-8 -*-
# 文件的写入write追加
fileObject=open("../../file/foo5.txt","a")
fileObject.write('''
你好;
我是;
Jerry!
''')
fileObject.close()