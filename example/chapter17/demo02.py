# -*- coding: UTF-8 -*-
from pojo.User import User
from pojo.Point import Point

user1=User("zhangsan",12)
user1.displayCount()
print "============================"
point1 = Point()
point2 = point1
point3 = point1
print id(point1),id(point2),id(point3)
del point1
del point2
del point3