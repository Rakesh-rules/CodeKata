n = int(input())
a = int(input())
d = int(input())
sum=0
count=a
for x in range(0,n):
    sum+=count
    count+=d
print(sum)
