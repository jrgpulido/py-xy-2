#
# derivation
# 
# numpy.org/doc/stable/reference/routines.polynomials.html
#
# legacy
# numpy.org/doc/stable/reference/generated/numpy.poly1d.html
# numpy.org/doc/stable/reference/generated/numpy.polyder.html
#

from numpy.polynomial import polynomial as P

# 1 + 2x + 3x**2 + 4x**3
c = (1,2,3,4) 

p=P.polyder(c) 

# (d/dx)(c) = 2 + 6x + 12x**2
print(p)
