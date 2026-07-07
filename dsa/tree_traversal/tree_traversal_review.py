'''
Tree Traversal Review

Implement:
1. BFS / Level Order
2. DFS Preorder
3. DFS Inorder
4. DFS Postorder
'''


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True

        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def BFS(self):
        queue = []
        results = []

        current_node = self.root

        queue.append(current_node)

        while len(queue) > 0:
            temp = queue.pop(0)
            results.append(temp.value)

            if temp.left is not None:
                queue.append(temp.left)

            if temp.right is not None:
                queue.append(temp.right)

        return results

    def dfs_pre_order(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)

            if current_node.left is not None:
                traverse(current_node.left)

            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)

        return results


    def dfs_in_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)

            results.append(current_node.value)

            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)

        return results

    def dfs_post_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)

            if current_node.right is not None:
                traverse(current_node.right)

            results.append(current_node.value)

        traverse(self.root)

        return results


def build_tree():
    tree = BinarySearchTree()
    for value in [47, 21, 76, 18, 27, 52, 82]:
        tree.insert(value)
    return tree


def check(name, actual, expected):
    print(name)
    print("Expected:", expected)
    print("Actual:  ", actual)
    print("PASS" if actual == expected else "FAIL")
    print()


my_tree = build_tree()
check("BFS", my_tree.BFS(), [47, 21, 76, 18, 27, 52, 82])

my_tree = build_tree()
check("DFS Preorder", my_tree.dfs_pre_order(), [47, 21, 18, 27, 76, 52, 82])

my_tree = build_tree()
check("DFS Inorder", my_tree.dfs_in_order(), [18, 21, 27, 47, 52, 76, 82])

my_tree = build_tree()
check("DFS Postorder", my_tree.dfs_post_order(), [18, 27, 21, 52, 82, 76, 47])


"""
    EXPECTED OUTPUT:
    ----------------
    All checks should print PASS.
"""
