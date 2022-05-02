n=int(input())
s=n*n
l=0
while s>0:
    d=s%10;
    l=l+d
    s=s//10
if l==n:
    print('Neon Number')
else:
    print('Not Neon Number')
