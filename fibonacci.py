num=int(input())
x=0
y=1
z=x+y
print(x,y,end=' ')
t=0
while z!=0:
    print(z,end=' ')
    x=y
    y=z
    z=x+y
    t+=1
    if(t==num-2):
        break