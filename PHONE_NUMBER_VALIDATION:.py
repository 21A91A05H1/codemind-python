a=int(input())
c=0
b=a
i=0
while a>0:
    c+=1
    a=a//10
if c==10:
    if b/1000000000==0:
        print('Invalid')
    else:
        print('Valid')
else:
    print('Invalid')