
#Implement Stack
print "Swaminarayan !!!"

class Stack():
    def __init__(self):
        self.A = []
    def push(self,ele):
        self.A.append(ele)
    def pop(self):
        if(self.isEmpty()):
            print "Stack underflow"
            return
        return self.A.pop()
    def peek(self):
        if(self.isEmpty()):
            print "Stack underflow"
            return
        return self.A[len(A)-1]
    def isEmpty(self):
        if(self.A == []):
            return True
        return False
    def size(self):
        return len(self.A)
    def printStack(self):
        print self.A



s = Stack()

s.isEmpty()

s.push(1)
s.push(2)
s.push(3)
s.push("adf")
s.printStack()
s.pop()
s.size()
