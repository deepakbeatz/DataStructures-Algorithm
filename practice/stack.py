class stack:    
    def __init__(self):
        self.stack=list()

    def push(self,k):
        self.stack.append(k)
    
    def pop(self):
        temp=self.stack.pop()
        return temp

    def print(self):
        print(self.stack)

s=stack()
s.push(10)
s.push(20)
s.push(40)
s.pop()
s.print()