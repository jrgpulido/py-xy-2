#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  5 20:52:00 2022

@author: jrgpulido
"""
# 
# to complete
#
from math import exp

def fn(x):
    return x-exp(2*x)+4

def ck(a,b):
    n=fn(b)*a - fn(a)*b
    d=fn(b) - fn(a)
    return n/d

#
# c_1
#
a=.5
b=1
print(ck(a,b))
#vs
print('%.6f '%ck(a,b))

#
# change interval
#

#
# then calculate next
# c_2
#
