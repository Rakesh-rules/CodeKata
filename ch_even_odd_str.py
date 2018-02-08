a=str(input())
lst=[]
for x in range(0,len(a),2):
    lst+=a[x+1]+a[x]
a="".join(lst[::1])
print(a)
