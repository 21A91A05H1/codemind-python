n=int(input())
t=0
for i in range(31):
    if 2**i==n:
        t=1
        break
if t==1:
    print('True')
else:
    print('False')