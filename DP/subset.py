set=[10,11,12,4,5,7]


sume={}
key={}
def subset(set,range):
    i,j=range;
    try:
        return sume[range]
    except:
        if(i==j):
            sume[(i,j)]=set[i]
            return set[i]
        else:
            sume[(i,j)]=subset(set,(i,j-1))+set[j]
            sume[(i,j)]=subset(set,(i+1,j))+set[i]
        if(sume[(i,j)]==16):
            key[(i,j)]=True
        return sume[(i,j)]

subset(set,(0,len(set)-1))
print(set)
print(key)
        
    
        
