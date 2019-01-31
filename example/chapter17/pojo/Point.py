# -*- coding: UTF-8 -*-
class Point:
    def __init__(self,a=0,b=0):
        self.a=a
        self.b=b
    def __del__(self):
        class_name=self.__class__.__name__
        print class_name,unicode("销毁",encoding="utf-8")