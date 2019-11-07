class tree:
    def __init__(self,data):
        self.data=data
        self.visited=False
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
            return self


t=tree(10)
t.insert(20)
t.insert(40)
t.insert(30)
t.insert(5)
t.insert(15)
t.insert(60)

def preorder(t):
    print(t.data)
    if(t.left!=None):
        preorder(t.left)
    if(t.right!=None):
        preorder(t.right)

def levelorder(root):
    if(root is None):
        return 
    q=[]
    r=[]
    count=0
    q.insert(0,(root,1))
    while(len(q)!=0):
        temp,depth=q.pop()
        depth=max(depth,count)
        temp.visited=True
        r.append(temp.data)
        if(temp.left!=None):
            q.insert(0,(temp.left,count+1))
        if(temp.right!=None):
            q.insert(0,(temp.right,depth+1))
        count+=1
    return count


d={
    'l':None,
    'r':None
}
def find(root,data):
    if(root is None):
        return 
    if(data==root.data):
        return True
    if(root.left!=None):
        d['l']= find(root.left,data)
    if(root.right!=None):
        d['r']= find(root.right,data)
    if(d['l']!=None):
        return d['l']
    else:
        return d['r']

print(find(t,34))

# if(find(t,30)!=None):
#     print('found')
# else:
#     print("not found")
        
def size(root):
    if(root is None):
        return 0
    return size(root.left)+size(root.right)+1


def height(root):
    if(root is None):
        return 0
    return max(height(root.left),height(root.right))+1

def zigzag(root):
    if(root is None):
        return
    currentlevel=[] 
    result=[]
    currentlevel.append(root)
    lefttoright=True
    while(len(currentlevel)!=0):
        nextlevel=[]
        levelresult=[]
        while(len(currentlevel)!=0):
            temp=currentlevel.pop()
            levelresult.append(temp.data)
            if(lefttoright):
                if(temp.left!=None):
                    nextlevel.insert(0,temp.left)
                if(temp.right!=None):
                    nextlevel.insert(0,temp.right)
            else:
                if(temp.right!=None):
                    nextlevel.insert(0,temp.right)
                if(temp.left!=None):
                    nextlevel.insert(0,temp.left)
        currentlevel=nextlevel
        result.append(levelresult)
        lefttoright=not(lefttoright)
    return result
        
print(zigzag(t))