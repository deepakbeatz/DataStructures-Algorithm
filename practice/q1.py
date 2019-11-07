from itertools import combinations
l=['a','b','c']

res=[]
for i in range(1,len(l)+1):
    p=list(combinations(l,i))
    for t in p:
        res.append("".join(list(t)))

print(res)