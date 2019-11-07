class tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.visited=False
    
    def insert(self,data):
        if(data<self.data):
            if(self.left==None):
                self.left=tree(data)
            else:
                self.left.insert(data)
        
        elif(data>self.data):
            if(self.right==None):
                self.right=tree(data)
            else:
                self.right.insert(data)

    def find(self,data):

        if(data<self.data):
            if(self.left==None):
                print("Not Found")
                return 
            else:
                return self.left.find(data)

        elif(data>self.data):
            if(self.right==None):
                print("Not Found")
                return 
            else:
                return self.right.find(data)

        else:
            print("found")
            return self

    def preorder(self):
        print(self.data)
        if(self.left!=None):
            self.left.preorder()
        if(self.right!=None):
            self.right.preorder()


t=tree(40)
t.insert(30)
t.insert(50)
t.insert(45)
t.insert(75)
print(t.find(45).visited)