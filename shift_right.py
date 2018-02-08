g=int(input())
k=int(input())
x = list()
for t in range(g):
    m=input()
    x.append(m)
b= [0]*(2*g)
for i in range(g):
    b[i] = x[i]
    b[g+i] = x[i]
c=abs(g-k)
print(c,b[c:c+g])
