n,m=map(int,input().split())
if n>m:
    t=m
    m=n
    n=t
h=0
for i in range(1,n+1,1):
    if n%i==0 and m%i==0:
        if h<i:
            h=i
print(h)