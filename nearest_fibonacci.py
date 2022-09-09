def nfib(num):
    if(num==0):
        print(0)
        return 0
    f=0
    s=1
    t=f+s
    while(t<=num):
        f=s
        s=t
        t=f+s
    if(abs(t-num)>=abs(s-num)):
        ans=s
    else:
        ans=t
    k=ans
    return k
def fi(nu):
    n1=0
    n2=1
    nefi=n1+n2
    while(nefi<=nu):
        n1=n2
        n2=nefi
        nefi=n1+n2
    return nefi
n=int(input())
nefi=fi(n)
k=nfib(n)
if((n-k)>(nefi-n)):
    print(nefi)
elif ((n-k)==(nefi-n)):
    print(k,nefi)
else:
    print(k)