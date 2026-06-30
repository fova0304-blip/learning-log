class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

          
    def __r_insert(self, current_node, value):
        if current_node == None: 
            return Node(value)   
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value) 
        return current_node    

    def r_insert(self, value):
        if self.root == None: 
            self.root = Node(value)
        self.__r_insert(self.root, value)  


    def min_value(self, current_node):
        while (current_node.left is not None):
            current_node = current_node.left
        return current_node.value 

    def __r_delete(self, current_node, value):
        if current_node == None:
            return None
        
        if value < current_node.value:
            current_node.left = self.__r_delete(current_node.left, value)
        
        elif value > current_node.value:
            current_node.right = self.__r_delete(current_node.right, value)

        else:
            if current_node.left == None and current_node.right == None:
                return None
            elif current_node.left == None: #and current_node.right != None
                current_node = current_node.right
            elif current_node.right == None: #and current_node.left != None
                current_node = current_node.left
            else:
                minimum_value = self.min_value(current_node.right)
                current_node.value = minimum_value
                current_node.right = self.__r_delete(current_node.right, minimum_value)
                '''
                current_node.right = self.__r_delete(current_node.right, minimum_value):
                
                recursion 써서 current_node.right 중 제일 작은애(minimum_value)를 None으로 바꿔주고
                (if current_node.left == None and current_node.right == None:
                    return None 에서 None으로 바꿔줌, 만약에 오른쪽이 있더라도 
                    example:       
                     8
                    /
                    6
                    \
                     7
                elif current_node.left == None: #and current_node.right != None
                    current_node = current_node.right로 처리 해줌)
                call stack 방식으로 current_node.right까지 다시 올라가기 
                그담에 current_node(value만 바뀜) 다시 리턴해주고 다시 콜스택으로 self.root까지 올라가기
                '''

        return current_node
    
    def delete_node(self,value):
        self.__r_delete(self.root, value)




##########################################################   
##   Test code below will print output to "User logs"   ##
##########################################################

def check(expect, actual, message):
    print(message)
    print("EXPECTED:", expect)
    print("RETURNED:", actual)
    print("PASS" if expect == actual else "FAIL", "\n")


# test_delete_node_no_children
print("\n----- Test: Delete node with no children -----\n")
bst = BinarySearchTree()
values = [5, 3, 8]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
bst.delete_node(3)
check(None, bst.root.left, "Left child of root after deleting 3:")


# test_delete_node_only_left_child
print("\n----- Test: Delete node with only left child -----\n")
bst = BinarySearchTree()
values = [5, 3, 8, 1]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
bst.delete_node(3)
check(1, bst.root.left.value, "Left child of root after deleting 3:")


# test_delete_node_only_right_child
print("\n----- Test: Delete node with only right child -----\n")
bst = BinarySearchTree()
values = [5, 3, 8, 9]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
bst.delete_node(8)
check(9, bst.root.right.value, "Right child of root after deleting 8:")


# test_delete_node_two_children
print("\n----- Test: Delete node with two children -----\n")
bst = BinarySearchTree()
values = [5, 3, 8, 1, 4, 7, 9]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
bst.delete_node(3)
check(4, bst.root.left.value, "Left child of root after deleting 3:")


# test_delete_root
print("\n----- Test: Delete root -----\n")
bst = BinarySearchTree()
values = [5, 3, 8]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
bst.delete_node(5)
check(8, bst.root.value, "Root value after deleting 5:")


# test_delete_non_existent_node
print("\n----- Test: Attempt to delete a non-existent node -----\n")
bst = BinarySearchTree()
values = [5, 3, 8]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
original_root_value = bst.root.value
bst.delete_node(10)
check(original_root_value, bst.root.value, "Root value after attempting to delete 10:")
