m=[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,0]]

def perimeter(m):
    table=[[0 for _ in range(len(m[0])+1)]for _ in range(len(m)+1)]
    for i in range(len(m)):
        for j in range(len(m[0])):
            if(m[i][j]==1):
                table[i+1][j+1]=min(table[i][j+1],table[i+1][j],table[i][j])+1
    return table

print(perimeter(m))