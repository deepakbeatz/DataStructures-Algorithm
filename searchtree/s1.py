# cook your dish here
class tree:
    def __init__(self,data):
        self.data=data
        self.visited=False
        self.left=None
        self.right=None
    
    def insert(self,data,i):
        if(self.data):
            if(data<self.data):
                i=2*i+1
                if(self.left==None):
                    self.left=tree(data)
                    return i
                else:
                    return self.left.insert(data,i)
            if(data>self.data):
                i=i*2+2
                if(self.right==None):
                    self.right=tree(data)
                    return i
                else:
                    return self.right.insert(data,i)
        else:
            self.data=data
            return i
                
    def delete(self,data,i):
        if(data<self.data):
            i=2*i+1
            if(self.left==None):
                return i 
            else:
                return self.left.delete(data,i)
        if(data>self.data):
            i=2*i+2
            if(self.right==None):
                return i
            else:
                return self.right.delete(data,i)
        if(data==self.data):
            self.data=None
            return i

t=tree(None)       
q=input()
if(q!=""):
    q=int(q)
    while(q>0):
        o,data=input().split()
        data=int(data)
        if(o=='i'):
            pos=t.insert(data,1)
        else:
            pos=t.delete(data,1)
        print(pos)
        q-=1
        
                
        