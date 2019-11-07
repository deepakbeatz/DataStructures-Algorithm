res=[]
def permute(s,l,r):
    if(l==r):
        res.append(''.join(s))
    else:
        for i in range(l,r+1):
            s[l],s[i]=s[i],s[l]
            permute(s,l+1,r)
            s[l],s[i]=s[i],s[l]

s="720"
s=list(s)
permute(s,0,len(s)-1)
print([int(x)%8==0 for x in list(set(res))].count(True))


