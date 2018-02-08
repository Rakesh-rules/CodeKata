 n=int(input())
list=[]
for i in range(0,n):
    y=int(input())
    list.append(y)
count=0
for i in list:
    for x in list:
        if i==x:
            count+=1
    if count==1:
        print(i)
