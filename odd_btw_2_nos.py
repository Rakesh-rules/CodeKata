a = int(input())
b = int(input())
s = ""
for x in range(a,b+1):
    if x%2!=0:
        s += str(x) + " "
print (s)
