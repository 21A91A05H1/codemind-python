s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
b=[]
c=0
for i in s1:
    if i  in s2:
        if ord(i) not in b:
            if i==' ':
                continue
            b.append(ord(i))
            c+=1
if c==0:
    print(-1)
else:
    b.sort()
    for i in b:
        print(chr(i),end='')
