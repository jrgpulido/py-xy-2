#
# derivation
# 
# numpy.org/doc/stable/reference/routines.polynomials.html
#
# LEGACY
# numpy.org/doc/stable/reference/generated/numpy.poly1d.html
# numpy.org/doc/stable/reference/generated/numpy.polyder.html
#

from numpy.polynomial import polynomial as P

# 1 + 2x + 3x**2 + 4x**3
p = (1,2,3,4) 

d=P.polyder(p) 
# (d/dx)(c) = 2 + 6x + 12x**2
print(d)
