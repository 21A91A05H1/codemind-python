n=int(input())
s=0
for i in range(1,n+1):
    s=s+(1/i)
f='{0:.2f}'.format(s)
print(f)