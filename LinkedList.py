
# coding: utf-8

# In[1]:

print "Swaminaryan!!"


# In[17]:

class Node():
    def __init__(self,val = None, nextnode = None):
        self.val = val
        self.nextnode = nextnode
    
    def setnext(self,node):
        self.nextnode = node
    
    def getval(self):
        return self.val
    
    def getnext(self):
        return self.nextnode


# In[23]:

class LinkedList():
    def __init__(self, size = 0, head = None):
        self._size = size
        self._head = head
        
    def insert(self,val):
        self.size += 1
        new_node = Node(val)
        #new_node.setval(val)
        if self._head == None:
            self._head = new_node
            return
        
        curr_node = self._head
        while curr_node.getnext() != None :
            curr_node = curr_node.getnext()
        
        curr_node.setnext(new_node)
        
    def print_list(self):
        curr_node = self._head
        
        while curr_node != None :
            print curr_node.getval()
            curr_node = curr_node.getnext()
            
    def size(self):
        return self.size()
           


# In[24]:

ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
#ll.print_list()

print ll.size()


# In[ ]:



