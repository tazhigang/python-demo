#coding:utf-8
fielObject=open("file.txt","r")
lines=fielObject.readlines()
for line in lines:
    line = line.strip() 
    print unicode("读取的数据为:",encoding="utf-8")," %s" % (line)
fielObject.close()