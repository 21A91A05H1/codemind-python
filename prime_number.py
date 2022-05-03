n=int(input())
fc=0
for i in range(1,n+1):
    if(n%i==0):
        fc+=1
for i in range (1,n+1):
    if fc>2:
        print('not a prime')
        break
    else:
        print('prime')
        break