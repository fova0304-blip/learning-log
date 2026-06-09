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

def reverse_string(word):
    ls = ""
    for i in range(len(word)):
        ls += word[-i-1]
    return ls

'''
i	-i - 1	word[-i-1]
0	-1	    "o"
1	-2	    "l"
2	-3	    "l"
3	-4	    "e"
4	-5	    "h"

ls = ""

i = 0 -> ls += word[-1] -> "o"
i = 1 -> ls += word[-2] -> "ol"
i = 2 -> ls += word[-3] -> "oll"
i = 3 -> ls += word[-4] -> "olle"
i = 4 -> ls += word[-5] -> "olleh"
'''
## WRITE REVERSE_STRING FUNCTION HERE ###
#                                       #
#  This is a separate function that is  #
#  not a method within the Stack class. #
#  Indent all the way to the left.      #
#                                       #
#########################################




my_string = 'hello'

print(reverse_string(my_string))



"""
    EXPECTED OUTPUT:
    ----------------
    olleh

"""
