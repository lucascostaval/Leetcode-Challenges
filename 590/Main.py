from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        lst = []
        self.postorder_tree(root, lst)
        return lst
    
    def postorder_tree(self, root: 'Node', lst: List[int]) -> None:
        if root is None:
            return
        if root.children is not None:
            for node in root.children:
                self.postorder_tree(node, lst)
        lst.append(root.val)


root = Node(1, [Node(3), Node(2), Node(4)])
root.children[0].children = [Node(5), Node(6)]
sol = Solution()
lst = sol.postorder(root)
print(lst)