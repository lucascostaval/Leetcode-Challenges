from typing import Optional

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        node1 = root.left
        node2 = root.right
        while node1 is not None and node2 is not None:
            node1.next = node2
            node1 = node1.right if node1.right is not None else node1.left
            node2 = node2.left if node2.left is not None else node2.right
        self.connect(root.left)
        self.connect(root.right)
        return root


def create_tree(levels: int, value=0) -> Node:
    if levels == 0:
        return None
    root = Node(value)
    root.left = create_tree(levels-1, value*2+1)
    root.right = create_tree(levels-1, value*2+2)
    return root

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.right.right = Node(5)
sol = Solution()
connected_tree = sol.connect(tree)
print("done")