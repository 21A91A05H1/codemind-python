n=int(input())
a=list(map(int,input().split()))
k=int(input())
s=0
for i in a:
        s=s+i
        if i==k:
            break
print(s)