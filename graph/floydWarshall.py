from graph import graph,vertex,edge

g=graph()
a=vertex('a')
b=vertex('b')
c=vertex('c')
d=vertex('d')
e=vertex('e')
f=vertex('f')

g.addvertex(a)
g.addvertex(b)
g.addvertex(c)
g.addvertex(d)
g.addvertex(e)
g.addvertex(f)

e1=edge((a,b),10)
e2=edge((c,b),20)
e3=edge((c,d),40)
e4=edge((c,e),65)
e5=edge((a,d),41)
e6=edge((c,f),65)

g.addedge(e1)
g.addedge(e2)
g.addedge(e3)
g.addedge(e4)
g.addedge(e5)
g.addedge(e6)

gmat=(g.getmatrix())

def floydWarshall(gmat):
    for k in range(len(gmat)):
        for i in range(len(gmat)):
            for j in range(len(gmat)):
                if(i==j):
                    gmat[i][j]=0
                else:
                    gmat[i][j]=min(gmat[i][j],(gmat[i][k]+gmat[k][j]))


    return gmat

print(floydWarshall(gmat))
                


