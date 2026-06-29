'''
Heap LeetCode Review - 2 Problems

Review problems:
1. Kth Smallest Element
2. Maximum Element in a Stream
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
        while True:
            max_index = index
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index

            if right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return

    def remove(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return max_value


'''
Problem 1: Kth Smallest Element

Given a list of integers nums and an integer k,
return the kth smallest element.
'''


def find_kth_smallest(nums, k):
    max_heap = MaxHeap()

    for num in nums:
        max_heap.insert(num)

        if len(max_heap.heap) > k:
            max_heap.remove()

    return max_heap.heap[0]



'''
Problem 2: Maximum Element in a Stream

Given a list of integers nums,
return a list where each element is the maximum value seen so far.
'''


def stream_max(nums):
    max_heap = MaxHeap()
    result = []

    for num in nums:
        max_heap.insert(num)
        result.append(max_heap.heap[0])

    return result


print("Problem 1: Kth Smallest Element")
kth_tests = [
    ([3, 2, 1, 5, 6, 4], 2, 2),
    ([6, 5, 4, 3, 2, 1], 3, 3),
    ([1, 2, 3, 4, 5, 6], 4, 4),
    ([3, 2, 3, 1, 2, 4, 5, 5, 6], 7, 5),
]

for nums, k, expected in kth_tests:
    result = find_kth_smallest(nums, k)
    print(result, result == expected)

print("\nProblem 2: Maximum Element in a Stream")
stream_tests = [
    ([], []),
    ([1], [1]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([1, 2, 2, 1, 3, 3, 3, 2, 2], [1, 2, 2, 2, 3, 3, 3, 3, 3]),
    ([-1, -2, -3, -4, -5], [-1, -1, -1, -1, -1]),
]

for nums, expected in stream_tests:
    result = stream_max(nums)
    print(result, result == expected)


"""
    EXPECTED OUTPUT:
    ----------------
    Problem 1: Kth Smallest Element
    2 True
    3 True
    4 True
    5 True

    Problem 2: Maximum Element in a Stream
    [] True
    [1] True
    [1, 2, 3, 4, 5] True
    [1, 2, 2, 2, 3, 3, 3, 3, 3] True
    [-1, -1, -1, -1, -1] True

"""
