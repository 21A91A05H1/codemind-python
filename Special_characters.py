s=input()
b=[]
for i in s:
    if i.isdigit():
        b.append(i)
c=0
for i in s:
    if i.isdigit() or i.isalpha():
        continue
    else:
        c+=1
e=[]
o=[]
for i in b:
    if int(i)%2==0:
        e.append(i)
    else:
        o.append(i)
if c%2==0:
    for i in range(len(e)):
        print(e[i],end='')
        print(o[i],end='')
    j=i+1
    while(j<len(o)):
        print(o[j],end='')
        j+=1
else:
    for i in range(len(o)):
        print(o[i],end='')
        print(e[i],end='')
    j=i+1
    while(j<len(e)):
        print(e[j],end='')
        j+=1