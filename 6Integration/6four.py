"""
Created on Thu May  12 21:42:31 2022

@author: mandrad
"""
#
# Integración numérica
# Regla de Simpson
#
from math import exp

def f(x):
    return exp(-x**2)

a=0
b=1
m=(a+b)/2
r4=((b-a)/6)*(f(a)+4*f(m)+f(b))

print('Regla de Simpson I=',r4)
