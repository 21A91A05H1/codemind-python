s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
d=[]
c=0
for i in s1.split():
    for j in s2.split():
        if i==j and s1.count(i)==1 and s2.count(j)==1:
            d.append(i)
print(len(d))