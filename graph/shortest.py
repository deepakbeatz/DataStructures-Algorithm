def short(m,n,s):
    g={}
    visited={}
    edge=[]
    vertices=[]
    for i in range(1,m+1):
        g[i]=[]
        vertices.append(i)
        visited[i]=False
    
    for i in range(n):
        e=[int(x) for x in input().split()]
        edge.append(e)
    
    for i in edge:
        v1,v2=i
        if(v1 not in g[v2]):
            g[v2].append(v1)
        if(v2 not in g[v1]):
            g[v1].append(v2)
    
    q=[]
    r=[]

    print(g)

    q.insert(0,s)

    while(len(q)!=0):
        temp=q.pop()
        visited[temp]=True
        r.append(temp)
        
        for i in g[temp]:
            if(not(visited[i])):
                q.insert(0,i)

    print(r)
    distance=[]
    for i in range(1,m+1):
        key=0
        for j in range(len(r)):
            if(i==r[j]):
                pos=j
                key=1
            j+=1
        if(key==1):
            distance.append(pos)
        else:
            distance.append(-1)

    return distance
        
        
print(short(4,3,2))
                

    

    
