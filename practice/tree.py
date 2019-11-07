class tree:

    l=None
    r=None;

    def __init__(self,data):
        self.data=data;
        self.left=None;
        self.right=None;
        self.visited=False;

    def find(self,data):
        if(data==self.data):
            return self
            
        if(self.left!=None):
            self.l=self.left.find(data)
        if(self.right!=None):
            self.r=self.right.find(data)

        if(self.l!=None):
            return self.l
        else:
            return self.r
    
    def insert(self,data1,pos,data2):
        temp=self.find(data1)
        if(pos=="l"):
            temp.left=tree(data2)
        elif(pos=="r"):
            temp.right=tree(data2)

    def construct(self,arr,root,i,n):
        if(i<n):
            ele=tree(arr[i])
            root=ele
            root.left=self.construct(arr,root.left,2*i+1,n)
            root.right=self.construct(arr,root.right,2*i+2,n)
        return root

t=tree(3)
t.insert(3,'l',1)
t.insert(3,'r',2)
t.insert(1,'l',4)
t.insert(2,'r',5)

print(t.right.right.data)

