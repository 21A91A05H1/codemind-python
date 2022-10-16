t=int(input())
while(t):
    n=int(input())
    l=len(str(n))
    b=[]
    while(n):
        d=n%10
        b.append(d)
        n=n//10
    a=b[::-1]
    s=0
    for i in range(l-1,-1,-1):
        c=(l-1)-i-1
        while a[i]:
            s=s+(2**c)*a[i]
            a[i]=a[i]//10
    print(int(2*s))
    t-=1