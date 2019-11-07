class tree:

    l=None
    r=None

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.visited=False

    def find(self,data):
        if(data==self.data):
            return self
        if(self.left!=None):
            self.l= self.left.find(data)
        if(self.right!=None):
            self.r= self.right.find(data)
        
        if(self.l!=None):
            return self.l
        else:
            return self.r

    def insert(self,data1,position,data2):
        temp=self.find(data1)
        if(position=="left"):
            temp.left=tree(data2) 
        elif(position=="right"):
            temp.right=tree(data2)


    def construct(self,arr,root,i,n):
        if i<n:
            temp = tree(arr[i])  
            root = temp  
            root.left = self.construct(arr, root.left, 2 * i + 1, n)  
            root.right = self.construct(arr, root.right, 2 * i + 2, n) 
        return root 
    

    

# t=tree(None)
# t=t.construct([10,20,30,40],None,0,4)
# # t.insert(70,"left",20)
# # t.insert(70,"right",40)
# # t.insert(20,"right",80)

# print((t.find(20)).data)




