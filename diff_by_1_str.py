a=input().upper()
b=input().upper()
m=len(a)
n=len(b)
count=0
if a==b:
  for x in range(a):
    if a[x]!=b[x]:
      count+=1
if count==1:
  print("yes")
else:
  print("no")
