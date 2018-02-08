str1=input()
str2=input()
m = len(str1)
n = len(str2)
s=1
if m != n:
    s=0
m = [False] * 100
map = [-1] * 100
for i in range(n):
    if map[ord(str1[i])] == -1:
        if m[ord(str2[i])] == True:
            s=0
        m[ord(str2[i])] = True
        map[ord(str1[i])] = str2[i]
    elif map[ord(str1[i])] != str2[i]:
        s=0
if s==1:
  print("yes")
else:
  print("no")        
