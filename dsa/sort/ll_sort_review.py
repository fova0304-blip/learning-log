class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
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

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def to_list(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next
        return values

    def print_list(self):
        values = self.to_list()
        if values:
            print(" -> ".join(str(value) for value in values))
        else:
            print("empty")

    def bubble_sort(self):

        if self.length < 2:
            return 

        for _ in range(self.length - 1):
            current = self.head
            while current.next is not None:
                if current.value > current.next.value:
                    temp = current.value
                    current.value = current.next.value
                    current.next.value = temp
                current = current.next

    def selection_sort(self):

        if self.length < 2:
            return 

        current = self.head

        while current is not None:
            min_node = current
            scan_node = current.next

            while scan_node is not None:
                if min_node.value > scan_node.value:
                    min_node = scan_node

                scan_node = scan_node.next

            if current.value != min_node.value:
                temp = current.value
                current.value = min_node.value
                min_node.value = temp

            current = current.next

    def insertion_sort(self):

        if self.length < 2:
            return 

        sort_ll = self.head
        current = self.head.next
        sort_ll.next = None

        while current is not None:
            next_of_current = current.next

            if current.value < sort_ll.value:
                current.next = sort_ll
                sort_ll = current

            else:
                scan = sort_ll

                while scan.next is not None and scan.next.value < current.value:
                    scan = scan.next

                current.next = scan.next
                scan.next = current

            current = next_of_current

        self.head = sort_ll

        temp = sort_ll
        while temp.next is not None:
            temp = temp.next
        self.tail = temp




def build_linked_list(values):
    linked_list = LinkedList()
    for value in values:
        linked_list.append(value)
    return linked_list


def check(method_name, values, expected):
    linked_list = build_linked_list(values)
    getattr(linked_list, method_name)()
    actual = linked_list.to_list()
    print(f"{method_name}({values})")
    print("EXPECTED:", expected)
    print("RETURNED:", actual)
    print("PASS" if actual == expected else "FAIL")
    print("-" * 40)


test_cases = [
    ([4, 2, 6, 5, 1, 3], [1, 2, 3, 4, 5, 6]),
    ([1, 2, 3, 4], [1, 2, 3, 4]),
    ([4, 3, 2, 1], [1, 2, 3, 4]),
    ([3, 1, 2, 3, 1], [1, 1, 2, 3, 3]),
    ([5], [5]),
    ([], []),
]


for sort_method in ["bubble_sort", "selection_sort", "insertion_sort"]:
    print(f"\n===== {sort_method} =====")
    for nums, sorted_nums in test_cases:
        check(sort_method, nums, sorted_nums)
