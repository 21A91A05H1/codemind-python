n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if a.count(i)<2:
        b.append(i)
b.sort()
print(*b)