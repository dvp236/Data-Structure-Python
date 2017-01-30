import ctypes

class DynamicArray(object):

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self,k):
        if not 0 <= k <self.n:
            return IndexError("Index K is out of bounds")

        return self.A[k]

    def append(self,ele):
        if self.n == self.capacity:
            self._resize()

        self.A[self.n] = ele
        self.n += 1

    def _resize(self):
        new_cap = self.capacity * 2
        B = self.make_array(new_cap)

        for i in range(self.n):
            B[i] = self.A[i]

        self.A = B
        self.capacity = new_cap


    def make_array(self, capacity):
        return (capacity * ctypes.py_object)()



arr = DynamicArray()


arr.append(1)
arr.append(2)

len(arr)
