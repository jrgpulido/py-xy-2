#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  5 21:52:00 2022

@author: mandrad
"""
#
# Método de Newton para calcular la raíz
# Función :  2-x+sin(2*x)
# Derivada:  -1+2cos(2*x)
# 

from math import sin,cos
def f(x):
    return 2-x+sin(2*x)
def f2(x):
    return -1+2*cos(2*x)

x0=1.5
x1=x0-f(x0)/f2(x0)
print('x1= %.6f '%x1)

x2=x1-f(x1)/f2(x1)
print('x2=',x2)

x3=x2-f(x2)/f2(x2)
print('x3=',x3)
print('valor=',f(x3))
print('La raíz es ',x3)

