#
# 2do
#

p1=(2,1.43)
p3=(3.2,2.79)
p4=(4,3.56)


def fn(p1,p3):
    a=(p3[1]-p1[1])/(p3[0]-p1[0])
    return a

print(fn(p1,p3))
