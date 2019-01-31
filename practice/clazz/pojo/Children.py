# -*- coding: UTF-8 -*-
from Parent import Parent
class Children(Parent):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print "children eating......."
    def pay(self):
        print "children playing......"