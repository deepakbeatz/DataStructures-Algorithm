class vertex:
    def __init__(self,data):
        self.data=data
        self.visited=False
        self.neighbours=[]

class edge:
    def __init__(self,data):
        self.data=data
        self.visited=False


class graph:
    def __init__(self):
        self.root=None
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
    

matrix=[['s','*','*'],['*',0,'*'],['*','*','d']]


def getgraph(matrix):
    i=0
    j=0
    g=graph()
    while(i<len(matrix) or j<len(matrix[0])):
        if(matrix[i][j]=='s'):
            g.root=vertex(matrix[i][j])
        if(j+1<len(matrix[0])):
            if(matrix[i][j+1]!=0):
                g.addedge(edge((vertex(matrix[i][j]),vertex(matrix[i][j+1]))))

        if(i+1<len(matrix)):
            if(matrix[i+1][j]!=0):
                g.addedge(edge((vertex(matrix[i][j]),vertex(matrix[i+1][j]))))
        
        if(j-1>=0):
            if(matrix[i][j-1]!=0):
                g.addedge(edge((vertex(matrix[i][j]),vertex(matrix[i][j-1]))))
        
        if(i-1>=0):
            if(matrix[i-1][j]!=0):
                g.addedge(edge((vertex(matrix[i][j]),vertex(matrix[i-1][j]))))
        
        i+=1
        j+=1

    return g 

root=getgraph(matrix)

print([x.data for x in root.vertices[2].neighbours])






