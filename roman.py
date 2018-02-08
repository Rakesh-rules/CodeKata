roman=input().upper()
values={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
res=0
for i in range(len(roman)):
        if i > 0 and values[roman[i]] > values[roman[i-1]]:
            res+=values[roman[i]]-2*values[roman[i-1]]
        else:
            res += values[roman[i]]
print(res)
