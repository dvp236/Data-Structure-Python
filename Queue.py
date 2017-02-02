

print "Thank you for blessings, Lord Swaminarayan !"



#implementation of queue. FIFO
class Queue():
    def __init__(self):
        self.A = []

    def enqueue(self,ele):
        #append items at the start
        self.A.insert(0,ele)
    def dequeue(self):
        return self.A.pop()
    def size(self):
        return len(self.A)
    def printQueue(self):
        print ",".join([str(v) for v in self.A[::-1]])



q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)



q.dequeue()


q.printQueue()



q.dequeue()


q.size()
