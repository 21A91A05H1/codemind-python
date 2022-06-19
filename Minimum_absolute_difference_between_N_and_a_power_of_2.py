n=int(input())
t=0
min=999
for i in range(1,n+1):
    t=abs(n-(2**i))
    if(min>t):
        min=t
print(min)