a=int(input())
b=int(input())
sum=0
for y in range(a+1,b):
    s=y
    c = len(str(s))
    for x in range(1,c+1):
        sum += (s%10)**c
        s=s/10
    if y==sum:
        print(y)
    sum=0
