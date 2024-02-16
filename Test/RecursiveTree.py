class Node:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root: Node = None

    def contains(self, x: int) -> bool:
        return self.__r_contains(x, self.root)

    def __r_contains(self, x: int, node: Node):
        if node is not None:
            if x == node.value: return True
            if x < node.value: return self.__r_contains(x, node.left)
            if x > node.value: return self.__r_contains(x, node.right)
        return False
    
    def r_insert(self, value):
        if self.root is None: self.root = Node(value)
        else: self.__r_insert(value, self.root)
        
    def __r_insert(self, value, node: Node):
        if node is None: return Node(value)
        if value < node.value: node.left = self.__r_insert(value, node.left)
        elif value > node.value: node.right = self.__r_insert(value, node.right)
        return node
            

tree = Tree()
tree.r_insert(3)
tree.r_insert(1)
tree.r_insert(2)
tree.r_insert(5)

