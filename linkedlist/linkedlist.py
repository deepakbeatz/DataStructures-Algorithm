class node:
    def __init__(self,data):
        self.data=data;
        self.next=None;

class linkedlist:
    def __init__(self,head):
        self.head=head
    
    def insert(self,k):
        node=self.head;
        while(node.next!=None):
            if(node.data!=k.data):
                node=node.next;
            else:
                print("data already present!!!")
                return 
        node.next=k 
    
    def print(self):
        node=self.head;
        while(node!=None):
            print(node.data+ "->",end="");
            node=node.next;
        print("none")

    def find(self,k):
        node=self.head;
        while(node!=None):
            if(node.data==k):
                return node
            else:
                node=node.next;
        return -1
    
    
        

    

l=linkedlist(node("a"));
l.insert(node("b"))
l.insert(node("c"))
l.insert(node("d"))
#element=""
# while(element!="exit"):
#     print("Enter the element:");
#     element=input()
#     if(element!="exit" and element!=""):
#         l.insert(node(element))
#         l.print()
#         print("")

node=l.find('g')





