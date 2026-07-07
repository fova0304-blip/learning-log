'''
Recursive BST / Binary Tree LeetCode Review - 2 Problems

Review problems:
1. Convert Sorted List to Balanced BST
2. Invert Binary Tree
'''


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        self.root = self.__r_insert(self.root, value)

    def inorder_traversal(self):
        result = []
        self.__inorder_helper(self.root, result)
        return result

    def __inorder_helper(self, node, result):
        if node is not None:
            self.__inorder_helper(node.left, result)
            result.append(node.value)
            self.__inorder_helper(node.right, result)

    def is_balanced(self):
        def check_balance(node):
            if node is None:
                return True, -1

            left_balanced, left_height = check_balance(node.left)
            if not left_balanced:
                return False, 0

            right_balanced, right_height = check_balance(node.right)
            if not right_balanced:
                return False, 0

            balanced = abs(left_height - right_height) <= 1
            height = 1 + max(left_height, right_height)
            return balanced, height

        balanced, _ = check_balance(self.root)
        return balanced

    def sorted_list_to_bst(self, nums):
        self.root = self.__sorted_list_to_bst(nums, 0, len(nums) - 1)

    def __sorted_list_to_bst(self, nums, left, right):

        if left > right:
            return None
        
        mid = (left + right) // 2
        
        current_node = Node(nums[mid])

        current_node.left = self.__sorted_list_to_bst(nums, left, mid - 1)
        current_node.right = self.__sorted_list_to_bst(nums, mid+1, right)

        return current_node

    def invert(self):
        self.root = self.__invert_tree(self.root)

    def __invert_tree(self, node):
        if node is None:
            return None
        
        temp = node.left
        node.left = node.right
        node.right = temp

        self.__invert_tree(node.left)
        self.__invert_tree(node.right)

        return node


def tree_to_list(node):
    if node is None:
        return []

    queue = [node]
    result = []

    while queue:
        current = queue.pop(0)
        if current is None:
            result.append(None)
        else:
            result.append(current.value)
            queue.append(current.left)
            queue.append(current.right)

    while result and result[-1] is None:
        result.pop()

    return result


def check(name, actual, expected):
    print(name)
    print("Expected:", expected)
    print("Actual:  ", actual)
    print("PASS" if actual == expected else "FAIL")
    print()


print("Problem 1: Convert Sorted List to Balanced BST")

bst = BinarySearchTree()
bst.sorted_list_to_bst([])
check("Empty list inorder", bst.inorder_traversal(), [])
check("Empty list balanced", bst.is_balanced(), True)

bst = BinarySearchTree()
bst.sorted_list_to_bst([10])
check("Single node inorder", bst.inorder_traversal(), [10])
check("Single node balanced", bst.is_balanced(), True)

bst = BinarySearchTree()
bst.sorted_list_to_bst([1, 2, 3, 4, 5])
check("Odd length inorder", bst.inorder_traversal(), [1, 2, 3, 4, 5])
check("Odd length balanced", bst.is_balanced(), True)

bst = BinarySearchTree()
bst.sorted_list_to_bst([1, 2, 3, 4, 5, 6])
check("Even length inorder", bst.inorder_traversal(), [1, 2, 3, 4, 5, 6])
check("Even length balanced", bst.is_balanced(), True)

print("Problem 2: Invert Binary Tree")

bst = BinarySearchTree()
bst.invert()
check("Invert empty tree", tree_to_list(bst.root), [])

bst = BinarySearchTree()
bst.r_insert(1)
bst.invert()
check("Invert single node", tree_to_list(bst.root), [1])

bst = BinarySearchTree()
for value in [2, 1]:
    bst.r_insert(value)
bst.invert()
check("Invert tree with left child", tree_to_list(bst.root), [2, None, 1])

bst = BinarySearchTree()
for value in [3, 1, 5, 2]:
    bst.r_insert(value)
bst.invert()
check("Invert multi-level tree", tree_to_list(bst.root), [3, 5, 1, None, None, 2])

bst = BinarySearchTree()
for value in [4, 2, 6, 1, 3, 5, 7]:
    bst.r_insert(value)
bst.invert()
bst.invert()
check("Invert twice", tree_to_list(bst.root), [4, 2, 6, 1, 3, 5, 7])


"""
    EXPECTED OUTPUT:
    ----------------
    All checks should print PASS.
"""
