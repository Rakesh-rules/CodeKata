a= int(input())
b = len(str(a))
sum=0
s=a
for x in range(1,b+1):
    sum += (s%10)**b
    s=s/10
if a==sum:
    print("yes")
else:
    print("no")
