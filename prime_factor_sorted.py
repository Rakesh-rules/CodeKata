n=int(input())
lst=[]
for x in range(2,n):
    if n%x==0:
        lst.append(x)
count=0
lst1=[]
for x1 in lst:
    for y in range(2,x1):
        if x1%y==0:
            pass
        else:
            count=1
    if count=1:
        lst1.append(x1)
    count=0
print(sorted(lst1))
