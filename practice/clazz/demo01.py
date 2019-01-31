# -*- coding: UTF-8 -*-
from pojo.Children import Children
from pojo.Parent import Parent

children = Children("as",22)
children.pay()

children.study()


parent = Parent("asf",42)
parent.pay()

print parent._Parent__des

parent._Parent__say()