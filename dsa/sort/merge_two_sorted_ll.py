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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def merge(self,l2):
        if self.length <= 0:
            return
        if l2.length <= 0:
            return 
        dummy = LinkedList(0)
        head1 = self.head
        head2 = l2.head

        while head1 is not None and head2 is not None:
            if head1.value < head2.value:
                dummy.append(head1.value)
                head1 = head1.next


            else:
                dummy.append(head2.value)
                head2 = head2.next

        while head1 is not None:
            dummy.append(head1.value)
            head1 = head1.next

        while head2 is not None:
            dummy.append(head2.value)
            head2 = head2.next


        self.head = dummy.head.next
        total_length = self.length + l2.length
        self.length = total_length

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        self.tail = temp



    


l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)


l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8

"""