def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
a=list(map(int,input().split()))
m=a.index(max(a))
n=a.index(min(a))
c=0
for i in range(min(m,n),max(m,n)+1):
    if prime(a[i]):
        c+=1
print(c)