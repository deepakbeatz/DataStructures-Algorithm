def LCS(X,Y):
    table=[[0 for _ in range(len(Y)+1)]for _ in range(len(X)+1)]
    for i,x in enumerate(X):
        for j,y in enumerate(Y):
            if(x==y):
                table[i+1][j+1]=table[i][j]+1
            else:
                table[i+1][j+1]=max(table[i][j+1],table[i+1][j])
    x,y=len(X),len(Y)
    res=""
    print(table)
    while(x!=0 and y!=0):
        if(table[x][y]==table[x-1][y]):
            x-=1;
        elif(table[x][y]==table[x][y-1]):
            y-=1;
        else:
            res=X[x-1]+res
            x-=1
            y-=1;
    return res

print(LCS(list("abcdgf"),list("bcdf")))