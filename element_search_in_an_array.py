n=int(input())
a=list(map(int,input().split()))
k=int(input())
c=0
for i in a:
    if i==k:
        c+=1
if c==0:
    print('False')
else:
    print('True')