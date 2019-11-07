class queue:
    def __init__(self):
        self.queue=list()

    def enqueue(self,k):
        self.queue.insert(0,k)
    
    def dequeue(self):
        return self.queue.pop()

    def print(self):
        print(self.queue)

q=queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.dequeue()
q.print()