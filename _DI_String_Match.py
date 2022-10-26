s=input()
b=[]
for i in range(len(s)+1):
    b.append(i)
l=[]
x=0
k=len(b)-1
for j in range(len(s)):
    if s[j]=='I':
        l.append(b[x])
        x+=1
    if s[j]=='D':
        l.append(b[k])
        k-=1
for i in b:
    if i not in l:
        l.append(i)
print(*l)