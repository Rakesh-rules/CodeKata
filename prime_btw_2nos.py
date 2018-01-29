a = int(input())
b = int(input())
flag = 0
for x in range(a+1,b):
  for y in range(2,x):
    if x%y==0:
        flag =1
  if flag == 0:
    print (x)
  flag = 0
