# cook your dish here
def csum(seq,r,k):
    i,j=r
    if(seq[i]+seq[j]==k):
        return True
    else:
        if(i<len(seq) and j>=0 and i!=j):
            if(seq[i]+seq[j]>k):
                return csum(seq,(i,j-1),k)
            else:
                return csum(seq,(i+1,j),k)
        else:
            return False
    


t=input()
t=int(t)
while(t>0):
    n,k=[int(x)for x in input().split()]
    seq=[int(x) for x in input().split()]
    seq.sort()
    if(csum(seq,(0,len(seq)-1),k)):
        print("Yes")
    else:
        print("No")
    t-=1

    