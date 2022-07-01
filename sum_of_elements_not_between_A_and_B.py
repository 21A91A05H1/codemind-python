n=int(input())
a=list(map(int,input().split()))
l,r=map(int,input().split())
s=0
for i in a:
    if i>=l and i<=r:
        continue
    else:
        s=s+i
print(s)