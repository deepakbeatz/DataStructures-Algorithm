class stack:
    def __init__(self):
        self.stack=list()

    def push(self,k):
        if(k not in self.stack):
            self.stack.append(k)

    def pop(self):
        if(len(self.stack)>0):
            return self.stack.pop()
    
    def print(self):
        print(self.stack)


s=stack()
s.push(5)
s.print()
s.push(6)
s.print()
s.pop()
s.print()
