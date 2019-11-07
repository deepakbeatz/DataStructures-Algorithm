vertices=['a','b','c','d']
edges=[('a','b'),('b','c'),('c','d'),('c','a'),('a','d')]

def shortest(vertices,edges):
    g={}
    visited={}
    vdict={}
    j=0
    matrix=[[9999]*len(vertices) for _ in range(len(vertices))]

    for i in vertices:
        g[i]=[];
        visited[i]=[];
        vdict[i]=j
        j+=1
    
    for e in edges:
        v1,v2=e
        if(v2 not in g[v1]):
            g[v1].append(v2)
        matrix[vdict[v1]][vdict[v2]]=1

    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if(i==j):
                    matrix[i][j]=0
                else:
                    matrix[i][j]=min(matrix[i][j],matrix[i][k]+matrix[k][j])

    print(matrix)


shortest(vertices,edges)
        