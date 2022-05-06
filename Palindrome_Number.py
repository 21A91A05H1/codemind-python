T=int(input())
t=1
while t<=T:
    n=int(input())
    s=n
    r=0
    while n>0:
        d=n%10
        n=n//10
        r=(r*10)+d
    if s==r:
        print('True')
    else:
        print('False')