c=0
x=int(input())
y=int(input())
if x > y:
    z = x
else:
    z = y
while (True):
    if ((z % x == 0) and (z % y == 0)):
        c = z
        break
    z += 1
print(c)
