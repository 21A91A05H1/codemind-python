s=input()
b=[]
for i in s:
    if i==' ':
      continue
    else:
      b.append(ord(i))
m=min(b)
n=max(b)
e=s.count(chr(m))
l=s.count(chr(n))
print(chr(m),e,chr(n),l)