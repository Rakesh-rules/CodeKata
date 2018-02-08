import collections
s=input()
m=collections.Counter(s).most_common(1)[0][0]
print(m)
