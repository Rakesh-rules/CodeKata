s=input()
l=[]
v=['a','e','i','o','u']
for i in s:
     if i in v:
        x=i.replace(i,'')
        l.append(x)
     else:
        l.append(i)
e=''.join(l)
print(e[::-1])
