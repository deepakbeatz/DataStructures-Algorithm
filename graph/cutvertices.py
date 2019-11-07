vertices=['a','b','c','d','e','f']
edges=[('a','b'),('a','c'),('b','d'),('b','e'),('e','f')]


g={}
visited={}

def cutVertices(vertices,edges):
    for i in vertices:
        g[i]=[]
        visited[i]=False

    for i in edges:
        v1,v2=i
        if(v1 not in g[v2]):
            g[v2].append(v1)
        if(v2 not in g[v1]):
            g[v1].append(v2)
        
    q=[]
    r=[]
    cut=[]
    q.append(vertices[0])
    while(len(q)!=0):
        temp=q.pop()
        r.append(temp)
        visited[temp]=True
        for i in g[temp]:
            if(not(visited[i])):
                q.append(i)
            else:
                if(i not in cut):
                    cut.append(i)

    return cut

print(cutVertices(vertices,edges))






    




