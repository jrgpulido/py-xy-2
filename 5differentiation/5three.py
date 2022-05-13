"""
Created on Thu May  11 20:42:11 2022

@author: mandrad
"""
# Derivada de primer orden
#Método3 para calcular Derivación Numérica
#

from math import sin

def f(x):
    return 2**(sin(x**3))

x0=1.7
h1=0.5
r1=(f(x0+h1/2)-f(x0-h1/2))/h1
print('r1=',r1)
#print('f(x0)',f(x0))
#print('f(x0+h1)',f(x0+h1))

h2=0.3
r2=(f(x0+h2/2)-f(x0-h2/2))/h2
print('r2=',r2)
#print('f(x0+h2)',f(x0+h2))

h3=0.001
r3=(f(x0+h3/2)-f(x0-h3/2))/h3
print('r3=',r3)

h4=0.000001
r4=(f(x0+h4/2)-f(x0-h4/2))/h4
print('r4=',r4)

h5=0.000000001
r5=(f(x0+h5/2)-f(x0-h5/2))/h5
print('r5=',r5)
