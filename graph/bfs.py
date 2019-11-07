from graph import vertex, edge, graph

a=vertex('a')
b=vertex('b')
c=vertex('c')
d=vertex('d')
e=vertex('e')
f=vertex('f')

e1=edge((a,b),10)
e2=edge((a,c),40)
e3=edge((b,e),10)
e4=edge((b,d),10)
e5=edge((d,f),10)

g=graph()
g.addvertex(a)
g.addvertex(b)
g.addvertex(c)
g.addvertex(d)
g.addvertex(e)
g.addvertex(f)

g.addedge(e1)
g.addedge(e2)
g.addedge(e3)
g.addedge(e4)
g.addedge(e5)

def bfs(root):
    if root is None:
        return 
    
    q=list()
    r=list()

    q.insert(0,root)

    while(len(q)!=0):
        node=q.pop()

        node.visited=True
        r.append(node)

        for i in node.neighbours:
            if(not(i.visited)):
                q.insert(0,i)

    return r

print([i.data for i in bfs(a)])

    