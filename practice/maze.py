def maze(arr,pos):
    n=len(arr)
    if(pos==(n-1,n-1)):
        return [pos]
    a,b=pos
    if(a+1<n):
        if(arr[a+1][b]==1):
            a1=maze(arr,(a+1,b))
            if(a1!=None):
                return [(a,b)]+a1
    if(b+1<n):
        if(arr[a][b+1]==1):
            b1=maze(arr,(a,b+1))
            if(b1!=None):
                return [(a,b)]+b1
        
print(maze([[1,1,0],[0,1,0],[0,0,1]],(0,0)))
    

