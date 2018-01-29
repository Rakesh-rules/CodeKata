a = int(input())
flag = 0
for x in range (2,a):
    if a%x==0:
        flag=1
        break
    else:
        pass
if flag==0:
    print ("YES")
else:
    print("NO")
