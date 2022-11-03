import math
x,y=map(int,input().split())
while (y != 0):
        carry = x & y 
        x = x ^ y
        y = carry << 1
print(x)