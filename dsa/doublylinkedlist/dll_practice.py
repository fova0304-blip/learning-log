"""
Doubly Linked List Practice

How to use:
1. Fill in the TODO methods inside DoublyLinkedList.
2. Run this file.
3. Check the printed PASS/FAIL results.
4. If something fails, inspect head, tail, next, prev, and length.

Do not look at dll.py while solving unless you are fully stuck.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value=None):
        if value is None:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1

    def to_list_forward(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(temp.value)
            temp = temp.next
        return values

    def to_list_backward(self):
        values = []
        temp = self.tail
        while temp is not None:
            values.append(temp.value)
            temp = temp.prev
        return values

    def append(self, value):
        # Problem 1:
        # Add a new node to the end of the DLL.
        # Return True.
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        # Problem 2:
        # Add a new node to the beginning of the DLL.
        # Return True.
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop(self):
        # Problem 3:
        # Remove and return the last node.
        # Return None if the list is empty.
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def pop_first(self):
        # Problem 4:
        # Remove and return the first node.
        # Return None if the list is empty.
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        # Problem 5:
        # Return the node at index.
        # Return None for invalid index.
        # Bonus: search from head or tail depending on which is closer.
        if index <0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length /2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        # Problem 6:
        # Change the value of the node at index.
        # Return True if successful, otherwise False.
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        # Problem 7:
        # Insert a new node at index.
        # index == 0 should prepend.
        # index == length should append.
        # Return True if successful, otherwise False.
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index-1)
        after = before.next
        before.next = new_node
        after.prev = new_node
        new_node.prev = before
        new_node.next = after
        self.length += 1
        return True

    def remove(self, index):
        # Problem 8:
        # Remove and return the node at index.
        # Return None for invalid index.
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp


def check(name, actual, expected):
    if actual == expected:
        print(f"PASS: {name}")
    else:
        print(f"FAIL: {name}")
        print(f"  expected: {expected}")
        print(f"  actual:   {actual}")


def check_node(name, node, expected_value):
    actual = None if node is None else node.value
    check(name, actual, expected_value)


def check_integrity(name, dll, expected_forward):
    check(f"{name} forward", dll.to_list_forward(), expected_forward)
    check(f"{name} backward", dll.to_list_backward(), list(reversed(expected_forward)))
    check(f"{name} length", dll.length, len(expected_forward))
    check(f"{name} head", None if dll.head is None else dll.head.value, None if not expected_forward else expected_forward[0])
    check(f"{name} tail", None if dll.tail is None else dll.tail.value, None if not expected_forward else expected_forward[-1])


def run_tests():
    print("\n--- Problem 1: append ---")
    dll = DoublyLinkedList()
    check("append return empty", dll.append(1), True)
    check("append return non-empty", dll.append(2), True)
    check_integrity("append", dll, [1, 2])

    print("\n--- Problem 2: prepend ---")
    dll = DoublyLinkedList()
    check("prepend return empty", dll.prepend(2), True)
    check("prepend return non-empty", dll.prepend(1), True)
    check_integrity("prepend", dll, [1, 2])

    print("\n--- Problem 3: pop ---")
    dll = DoublyLinkedList()
    check_node("pop empty", dll.pop(), None)
    dll.append(1)
    dll.append(2)
    check_node("pop returns tail", dll.pop(), 2)
    check_integrity("pop after removing tail", dll, [1])
    check_node("pop last node", dll.pop(), 1)
    check_integrity("pop empty after last", dll, [])

    print("\n--- Problem 4: pop_first ---")
    dll = DoublyLinkedList()
    check_node("pop_first empty", dll.pop_first(), None)
    dll.append(1)
    dll.append(2)
    check_node("pop_first returns head", dll.pop_first(), 1)
    check_integrity("pop_first after removing head", dll, [2])
    check_node("pop_first last node", dll.pop_first(), 2)
    check_integrity("pop_first empty after last", dll, [])

    print("\n--- Problem 5: get ---")
    dll = DoublyLinkedList()
    for value in [10, 20, 30, 40, 50]:
        dll.append(value)
    check_node("get invalid negative", dll.get(-1), None)
    check_node("get invalid too large", dll.get(5), None)
    check_node("get head", dll.get(0), 10)
    check_node("get middle", dll.get(2), 30)
    check_node("get tail", dll.get(4), 50)

    print("\n--- Problem 6: set_value ---")
    dll = DoublyLinkedList()
    for value in [1, 2, 3]:
        dll.append(value)
    check("set invalid", dll.set_value(5, 99), False)
    check("set valid", dll.set_value(1, 99), True)
    check_integrity("set_value", dll, [1, 99, 3])

    print("\n--- Problem 7: insert ---")
    dll = DoublyLinkedList()
    check("insert invalid negative", dll.insert(-1, 99), False)
    check("insert invalid too large", dll.insert(1, 99), False)
    check("insert at empty head", dll.insert(0, 2), True)
    check("insert at head", dll.insert(0, 1), True)
    check("insert at tail", dll.insert(2, 4), True)
    check("insert in middle", dll.insert(2, 3), True)
    check_integrity("insert", dll, [1, 2, 3, 4])

    print("\n--- Problem 8: remove ---")
    dll = DoublyLinkedList()
    check_node("remove empty", dll.remove(0), None)
    for value in [1, 2, 3, 4, 5]:
        dll.append(value)
    check_node("remove invalid negative", dll.remove(-1), None)
    check_node("remove invalid too large", dll.remove(5), None)
    check_node("remove head", dll.remove(0), 1)
    check_integrity("remove after head", dll, [2, 3, 4, 5])
    check_node("remove tail", dll.remove(3), 5)
    check_integrity("remove after tail", dll, [2, 3, 4])
    check_node("remove middle", dll.remove(1), 3)
    check_integrity("remove after middle", dll, [2, 4])


if __name__ == "__main__":
    run_tests()
