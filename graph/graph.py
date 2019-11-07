class vertex:
    def __init__(self,data):
        self.data=data
        self.visited=False
        self.neighbours=[]

class edge:
    def __init__(self,data,weight):
        self.data=data;
        self.weight=weight;
        self.visited=False;

INF=9999

class graph:

    def __init__(self):
        self.vertices=[]
        self.edges=[]
        

    def addvertex(self,vertex):
        if(vertex not in self.vertices):
            self.vertices.append(vertex)

    def addedge(self,edge):
        if(edge not in self.edges):
            self.edges.append(edge)

        v1,v2=edge.data

        if(v1 not in self.vertices):
            self.vertices.append(v1)
        if(v2 not in v1.neighbours):
            v1.neighbours.append(v2)
                
        if(v2 not in self.vertices):
            self.vertices.append(v2)
        if(v1 not in v2.neighbours):
            v2.neighbours.append(v1)

    def vdict(self):
        dict={}
        j=0
        for i in self.vertices:
            dict[i]=j
            j+=1
        return dict 

    def getmatrix(self):
        dict=self.vdict()
        n=len(self.vertices)
        matrix=[[INF]*n for _ in range(n)];
        for edge in self.edges:
            i,j=edge.data;
            matrix[dict[i]][dict[j]]=edge.weight
            matrix[dict[j]][dict[i]]=edge.weight
        return matrix
    
    def getdict(self):
        gdict={}
        for i in self.vertices:
            gdict[i]=i.neighbours
        return gdict


g=graph()
a=vertex('a')
b=vertex('b')
c=vertex('c')
e1=edge((a,b),100)
e2=edge((a,c),50)
g.addvertex(a)
g.addvertex(b)
g.addedge(e1)
g.addedge(e2)
# print([{v1.data,v2.data} for v1,v2 in [x.data for x in g.edges]])
# print([x.weight for x in g.edges])
print(g.getdict())
