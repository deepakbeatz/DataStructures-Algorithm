from searchtree import tree


def preorder(t):
    print(t.data)
    
    if(t.left!=None):
        preorder(t.left)
    
    if(t.right!=None):
        preorder(t.right)

    

t=tree(40)
t.insert(50)
t.insert(60)
t.insert(55)
t.insert(65)


preorder(t)