'''
Max Heap Review

Implement:
1. insert(value)
2. _sink_down(index)
3. remove()

Max Heap rule:
Parent value should be greater than or equal to child values.
'''


class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def _sink_down(self, index):
        max_index = index

        while True:
            left_index = self._left_child(max_index)
            right_index = self._right_child(max_index)

            if (left_index < len(self.heap) and 
                self.heap[left_index] > self.heap[max_index]):
                max_index = left_index

            if (right_index < len(self.heap) and
                self.heap[right_index] > self.heap[max_index]):
                max_index = right_index

            if max_index != index:
                self._swap(max_index, index)
                index = max_index
            else:
                return


    def remove(self):
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_heap = self.heap[0]

        self.heap[0] = self.heap.pop()

        self._sink_down(0)

        return max_heap


print("Insert Review")
myheap = MaxHeap()
myheap.insert(99)
myheap.insert(72)
myheap.insert(61)
myheap.insert(58)
print(myheap.heap)

myheap.insert(100)
print(myheap.heap)

myheap.insert(75)
print(myheap.heap)

print("\nRemove Review")
myheap = MaxHeap()
myheap.insert(95)
myheap.insert(75)
myheap.insert(80)
myheap.insert(55)
myheap.insert(60)
myheap.insert(50)
myheap.insert(65)
print(myheap.heap)

print(myheap.remove())
print(myheap.heap)

print(myheap.remove())
print(myheap.heap)

print(myheap.remove())
print(myheap.heap)

print("\nEdge Cases")
empty_heap = MaxHeap()
print(empty_heap.remove())
empty_heap.insert(10)
print(empty_heap.remove())
print(empty_heap.heap)


"""
    EXPECTED OUTPUT:
    ----------------
    Insert Review
    [99, 72, 61, 58]
    [100, 99, 61, 58, 72]
    [100, 99, 75, 58, 72, 61]

    Remove Review
    [95, 75, 80, 55, 60, 50, 65]
    95
    [80, 75, 65, 55, 60, 50]
    80
    [75, 60, 65, 55, 50]
    75
    [65, 60, 50, 55]

    Edge Cases
    None
    10
    []

"""
