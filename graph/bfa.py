vertices=['a','b','c','d']
edges=[('a','b'),('b','c'),('c','d'),('c','a'),('a','d')]

def bfs(vertices,edges):
    g={}
    visited={}

    for i in vertices:
        g[i]=[]
        visited[i]=False

    for e in edges:
        v1,v2=e
        if(v2 not in g[v1]):
            g[v1].append(v2)
        
    q=[]
    r=[]
    q.insert(0,vertices[0])
    while(len(q)!=0):
        temp=q.pop()
        r.append(temp)
        visited[temp]=True
        for i in g[temp]:
            if(not(visited[i])):
                q.insert(0,i)
    print(r)

bfs(vertices,edges)