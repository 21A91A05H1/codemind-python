s=input()
c=0 
b=[]
for i in s:
    if i not in b:
        b.append(i)
    else:
        c=1
if c==0:
    print('True')
else:
    print('False')