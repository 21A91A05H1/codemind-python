t=int(input())
while t:
    m,n=map(int,input().split())
    f=-1
    for i in range(0,n+1):
        if (i*i)%n==m:
            f=i
            break
    print(f)
    t-=1