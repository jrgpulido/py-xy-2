"""
Created on Thu May  12 21:12:31 2022

@author: mandrad
"""
#
# Integración numérica
#Regla del Trapecio
#
from math import exp

def f(x):
    return exp(-x**2)

a=0
b=1
r3=((b-a)/2)*(f(a)+f(b))

print('Regla del Trapecio I=',r3)
