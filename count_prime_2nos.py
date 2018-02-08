a1 = int(input())
b1 = int(input())
flag = 0
count=0
for x in range(a1,b1+1):
  for y in range(2,x):
    if x%y==0:
        flag =1
  if flag == 0:
    count+=1
  flag = 0
print(count)  
