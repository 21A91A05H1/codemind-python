n,k=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in a:
    if(i%k==0):
        continue
    else:
        c+=1
print(c)