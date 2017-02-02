print "jsn"

#implementation of Deque. supports FIFO and LIFO
#Hybrid - combination of stack & queues
class Deque():
    def __init__(self):
        self.A = []

    def addFront(self,ele):
        #append items at the start
        self.A.insert(0,ele)
    def addRear(self,ele):
        #append items at the start
        self.A.append(ele)
    def removeFront(self):
        return self.A.pop(0)
    def removeRear(self):
        return self.A.pop()
    def isEmpty(self):
        return self.A == []
    def size(self):
        return len(self.A)


# In[3]:

d = Deque()


d.addFront(2)
d.addFront(1)
d.addRear(3)

d.removeFront()


d.removeRear()


d.size()


d.isEmpty()
