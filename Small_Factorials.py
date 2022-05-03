T=int(input())
t=1
fac=1
while t<=T:
    n=int(input())
    while n>0:
        fac=fac*n
        n-=1
    print(fac)
    fac=1
    t+=1