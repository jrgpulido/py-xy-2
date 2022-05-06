#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  5 21:52:00 2022

@author: mandrad
"""
#
# Método de la secante
# Función  2-x+sin(2*x)=0, calcular raíz
# Derivada  -1+2cos(2*x)
# 

from math import sin
def f(x):
    return 2-x+sin(2*x)

x4=1.7
x5=1.8
x6=x5-((x5-x4)/(f(x5)-f(x4)))*f(x5)
print('x6=',x6)
print('f(x4)=',f(x4))
print('f(x5)=',f(x5))
print('f(x6)=',f(x6))

#Se hace la sig. iteración con x4 y x6
#porque pasa de positivo a negativo en la función
x7=x6-((x6-x4)/(f(x6)-f(x4)))*f(x6)
print('x7=',x7)    
print('f(x4)=',f(x4))
print('f(x7)=',f(x7))

#
# y así continúa
#
