# -*- coding: UTF-8 -*-
# 判断1~20之间的整数是奇数还是偶数
for num in range(1,20):
    if num <=3:
        print num,unicode("是质数",encoding="utf-8")
    else:
        bool=False
        for var in range(2,num/2+1):
            if num%var==0 and num!=var:
                bool=True
                continue
        if bool:
            print num,unicode("是合数",encoding="utf-8")
        else:
            print num,unicode("是质数",encoding="utf-8")            