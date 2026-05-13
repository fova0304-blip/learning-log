class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def has_loop(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None: 
            '''
            결국 self.tail or None까지 갈수있냐 없냐가 관건임- None까지 못가면 slow,fast는 언젠가 만남
            while fast is not none and fast is not self.tail중  fast is not self.tail은 루프가 있으면 fast가 tail에 닿을수있으니 안됨
            관건은 None에 갈수있냐 없냐가 중요함
            '''

            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    
    
my_linked_list_1 = LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)
my_linked_list_1.tail.next = my_linked_list_1.head
print(my_linked_list_1.has_loop() ) # Returns True

my_linked_list_2 = LinkedList(1)
my_linked_list_2.append(2)
my_linked_list_2.append(3)
my_linked_list_2.append(4)
print(my_linked_list_2.has_loop() ) # Returns False

my_linked_list_3 = LinkedList(1)
my_linked_list_3.append(2)
my_linked_list_3.append(3)
my_linked_list_3.tail.next = my_linked_list_3.head
print(my_linked_list_3.has_loop() ) # Returns True

"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    
"""
