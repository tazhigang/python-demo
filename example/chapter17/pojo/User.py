# -*- coding: UTF-8 -*-
# python高级篇--对象
class User:
    count=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        User.count += 1
    def displayCount(self):
        print "the total count is %d" % (self.count)
    def disUser(self):
        print "count:%d ; name:%s ;age: %d" % (self.count,self.name,self.age)

# user1=User("zhangsan",12)
# user2=User("lisi",22)
# user3=User("zhaow",33)
# user1.displayCount() #
# user2.displayCount()
# user1.name="zhangss" #修改或者添加属性
# user1.disUser()
# #删除属性
# del user1.age

# print User.__name__
# print user1.__class__.__name__
# print User.__dict__