from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return
        if root.left is not None:
            tmp: TreeNode = root.right
            root.right = root.left
            tail: TreeNode = self.get_tail(root.left)
            tail.right = tmp
            root.left = None
        self.flatten(root.right)
            
    def get_tail(self, root: TreeNode) -> TreeNode:
        tail = root
        while tail.right != None:
            tail = tail.right
        return tail
    

def print_pre_order(root: TreeNode):
    if root != None:
        print(root.val)
        print_pre_order(root.left)
        print_pre_order(root.right)

def tree_insert(root: TreeNode, x: int) -> TreeNode:
    if root == None:
        return TreeNode(x)
    current = root
    parent = None
    isLeft = False
    while current != None:
        parent = current
        if x > current.val:
            current = current.right
            isLeft = False
        else:
            current = current.left
            isLeft = True
    new_node = TreeNode(x)
    if isLeft:
        parent.left = new_node
    else:
        parent.right = new_node
    return root

arr = [4, 2, 5, 3, 7, 6]
root = None
for x in arr:
    root = tree_insert(root, x)
sol = Solution()
sol.flatten(root)
print_pre_order(root)