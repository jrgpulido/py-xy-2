#
# integration
#
# numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyint.html
# numpy.org/doc/stable/reference/generated/numpy.trapz.html
#
# legacy
# numpy.org/doc/stable/reference/generated/numpy.polyint.html
#

from numpy.polynomial import polynomial as P

c = (1,2,3)

p = P.polyint(c) 

# should return array([0, 1, 1, 1])
print(p)
