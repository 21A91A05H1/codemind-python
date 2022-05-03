x=int(input())
y=int(input())
s=0
for i in range(1,x):
    if x%i==0:
        s=s+i
if s==y:
    print('Amicable')
else:
    print('Not Amicable')