n = int(input())
k = int(input())
arr = []
sum = 0
for x in range(n):
  arr.append(int(input()))
  if x<k:
    sum += arr[x]
print(sum)
