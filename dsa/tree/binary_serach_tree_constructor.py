class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

        
# 트리는 첫 번째 값이 들어오기 전까지 root가 뭔지 정할 수 없기 때문
class BinarySearchTree:
    def __init__(self):
        self.root = None


my_tree = BinarySearchTree()

print("Root:", my_tree.root)


 
"""
    EXPECTED OUTPUT:
    ----------------
    Root: None

"""