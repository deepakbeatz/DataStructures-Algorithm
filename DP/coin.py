def getCoins(coin,change):
    min=[0 for _ in range(change+1)]
    for i in range(change+1):
        count=i
        for j in [c for c in coin if c<=i]:
            if(min[i-j]+1<count):
                count=min[i-j]+1
        min[i]=count
    return min[change]
    
print(getCoins([1,1,1,1,7,10,10,20,20],31))