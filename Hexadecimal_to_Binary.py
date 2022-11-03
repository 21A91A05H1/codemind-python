t=int(input())
while(t):
    s=input()
    l=""
    for i in s:
        if i.isdigit():
            i=int(i)
            b={'{0:04b}'.format(i)}
            for i in b:
                l+=str(i)
        else:
            if i=='A':
                c=10
                b={'{0:04b}'.format(c)}
                for i in b:
                    l+=str(i)
            elif i=='B':
                c=11
                b={'{0:04b}'.format(c)}
                for i in b:
                    l+=str(i)
            elif i=='C':
                c=12
                b={'{0:04b}'.format(c)}
                for i in b:
                    l+=str(i)
            elif i=='D':
                c=13
                b={'{0:04b}'.format(c)}
                for i in b:
                    l+=str(i)
            elif i=='E':
                c=14
                b={'{0:04b}'.format(c)}
                for i in b:
                    l+=str(i)
            elif i=='F':
                c=15
                b={'{0:04b}'.format(c)}
                for i in b:
                    l+=str(i)
    print(l)
    t-=1