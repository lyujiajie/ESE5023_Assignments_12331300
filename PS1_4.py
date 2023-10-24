

#problem4
import random
import math
def Least_moves(y):
    for i in range(2,100):
        z=math.pow(2, i)
        if y>z:
            i=i+1
        else:
            break
    s=y-(2**(i-1))+(i-1)
    return s

for i in range(10):
  y = random.randint(1, 100)
  p=Least_moves(y)
  print(p)
