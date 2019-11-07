class queue:
    def __init__(self):
        self.queue=list()

    def enqueue(self,k):
        if(k not in self.queue):
            self.queue.insert(0,k)

    def dequeue(self):
        if(len(self.queue)>0):
            return self.queue.pop();

    def print(self):
        print(self.queue)


q=queue()
q.enqueue(5)
q.print()      
q.enqueue(6)
q.print()
q.dequeue()
q.print()

