# -*- coding: UTF-8 -*-
class Parent:
    __des="asd"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print "Parent eating......."
    def pay(self):
        print "Parent playing......"
    def study(self):
        print "Parent: %s %d" % (self.name,self.age)
    def __say(self):
        print "parent say....."