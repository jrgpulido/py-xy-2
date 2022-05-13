"""
Created on Thu May  12 20:42:31 2022

@author: mandrad
"""
#
# Integración numérica
# Regla del Rectángulo
#
from math import exp

def f(x):
    return exp(-x**2)

a=0
b=1
r1=f(a)*(b-a)

print('Regla del Rectángulo I=',r1)
