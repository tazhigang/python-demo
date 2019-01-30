# -*- coding: UTF-8 -*-
#continue 与 break的区别
count=1
while count<100:
    if count%2==0:
        print count,unicode("是偶数",encoding="utf-8")
    else:
        print count,unicode("是奇数",encoding="utf-8")
    count+=1

print unicode("下面是测试continue的用法",encoding="utf-8")
count=0
while count<100:
    count+=1
    if count%2==0:
         print count,unicode("是偶数",encoding="utf-8")
    else:
        continue
else:
    print unicode("测试while的基本循环结束",encoding="utf-8")
print unicode("下面是测试break的用法",encoding="utf-8")
count=0
while count<100:
    count+=1
    if count%2==0 and count==50:
         print count,unicode("是偶数",encoding="utf-8")
         break
    else:
        continue