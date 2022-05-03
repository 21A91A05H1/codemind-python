n,m=map(int,input().split())
if(n<m):
    t=n
    n=m
    m=t
min=0
for i in range(1,m+1):
    if n%i==0 and m%i==0:
        if i>min:
            min=i
hcf=min
lcm=(n*m)//hcf
print(lcm)