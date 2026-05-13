class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    def find_middle_node(self):
        slow = self.head
        fast = self.head
        
        while fast != self.tail and fast != None:
            fast = fast.next.next
            slow = slow.next
            
        return slow

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


print( my_linked_list.find_middle_node().value )


'''
total_length = n

slow 이동 거리 = x
fast 이동 거리 = 2x

2x ≈ n 일 때 → x ≈ n/2
'''