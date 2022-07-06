n=int(input())
a=list(map(int,input().split()))
s=0
c=0
for i in range(0,int((n/2))):
    s=s+a[i]
for j in range(int((n/2)),n):
    c=c+a[j]
print(c-s)