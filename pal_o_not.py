a = str(input())
y=len(a)-1
flag = 0
for x in range(len(a)):
    if a[x] == a[y]:
        pass
    else:
        flag =1
    if y>=0:
        y-=1
if flag==1:
    print ("NO")
else:
    print("YES")
