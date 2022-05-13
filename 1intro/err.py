#
# series
# 1/2 = 1/(1*3) + 1/(3*5) + 1/(5*7) + ...
#

s=0
for k in range(1,7,2):
#for k in range(1,15,2):
#for k in range(1,25,2):
    s+=1/(k*(k+2))
    print(k,s)
    
