r=int(input())
a=[list(map(int,input().split())) for i in range(r)]
s=0
c=0
t=0
c=r
for i in range(r):
    for j in range(c):
        if i==j:
            s=s+a[i][j]
for i in range(r):
    t=t+a[i][r-i-1]
print('Principal Diagonal:'+str(s))
print('Secondary Diagonal:'+str(t))