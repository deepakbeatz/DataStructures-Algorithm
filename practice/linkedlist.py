class node:
    def __init__(self,data):
        self.data=data;
        self.next=None;

class linkedlist:
    def __init__(self,head):
        self.head=head;
    
    def insert(self,node1):
        node=self.head;
        while(node.next!=None):
            node=node.next
        node.next=node1

    def print(self):
        node=self.head
        while(node!=None):
            print(str(node.data)+"->",end="")
            node=node.next
        print(None)


l=linkedlist(node(10))
l.insert(node(20))
l.print()