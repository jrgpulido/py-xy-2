"""
Created on Thu May  12 21:42:31 2022

@author: mandrad
"""
#
# Integración numérica
#Regla del Punto medio
#
from math import exp

def f(x):
    return exp(-x**2)

a=0
b=1
m=(a+b)/2
r2=f(m)*(b-a)

print('Regla del punto medio I=',r2)
