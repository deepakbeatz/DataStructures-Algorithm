class tree():
    def __init__(self,data):
        self.data=data;
        self.visited=False;
        self.left=None
        self.right=None

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
            if(self.left == None):
                print("Not Found")
                return 
            else:
                return self.left.find(data)
        elif(data>self.data):
            if(self.right == None):
                print("Not Found")
                return 
            else:
                return self.right.find(data)
        else:
            print("found")
            return self



