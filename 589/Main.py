from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        lst: List[int] = []
        self.preorder_tree(root, lst)
        return lst

    def preorder_tree(self, root, lst: List[int]):
        if root != None:
            lst.append(root.val)
            for child in root.children:
                self.preorder_tree(child, lst)