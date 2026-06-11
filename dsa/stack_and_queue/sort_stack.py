class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()

def sort_stack(stack_list):
    sorted_list = Stack()

    while not stack_list.is_empty(): #temp = stack_list.pop() 에서 오류나면 안됨
        temp = stack_list.pop()

        #while not sorted_list.is_empty():
        #맨 처음에 sorted_list가 비어있기 때문이기도 하고, 더 중요하게는 peek()를 안전하게 쓰려고 넣는 거

        while not sorted_list.is_empty() and sorted_list.peek() > temp: 
            ''' 
            temp보다 큰 애들 전부 stack_list로 빼기
                → temp를 sorted_list에 넣기
                → 다시 stack_list에서 하나 꺼내기
                → 반복
            '''

            stack_list.push(sorted_list.pop())
        
        sorted_list.push(temp) #다 옮기고 끝나면 그때서야 sort_list에 넣어주고 무한반복

    while not sorted_list.is_empty():
    #stack_list: empty아
    #sorted_list: full
        stack_list.push(sorted_list.pop())

    return stack_list







##### WRITE SORT_STACK FUNCTION HERE #####
#                                        #
#  This is a separate function that is   #
#  not a method within the Stack class.  #
#                                        #
#  <- INDENT ALL THE WAY TO THE LEFT <-  #
#                                        #
##########################################




my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()



"""
    EXPECTED OUTPUT:
    ----------------
    Stack before sort_stack():
    2
    4
    5
    1
    3

    Stack after sort_stack:
    1
    2
    3
    4
    5

"""