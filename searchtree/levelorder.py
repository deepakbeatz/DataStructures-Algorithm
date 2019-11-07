from searchtree import tree

tree=tree(40)
tree.insert(30)
tree.insert(60)
tree.insert(35)
tree.insert(50)
tree.insert(34)

def levelorder(tree):
    if tree is None:
        return
    
    q=list()
    r=list()
    q.insert(0,tree)

    while(len(q)!=0):
        node=q.pop()
        r.append(node)
        if(node.left!=None):
            q.insert(0,node.left)
        if(node.right!=None):
            q.insert(0,node.right)

    return r

l=levelorder(tree)
print([x.data for x in l][-1])