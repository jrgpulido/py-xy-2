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

#
# change interval
#

#
# c_2
#
a=.5
b=1
print(ck(a,b))
