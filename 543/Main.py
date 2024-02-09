from typing import Dict

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        h = {}
        h[None] = 0
        self.find_max_depth(root, h)
        result = -1
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            result = max(result, h[node.right]+h[node.left])
            if node.right is not None: stack.append(node.right)
            if node.left is not None: stack.append(node.left)
        return result

    def find_max_depth(self, root: TreeNode, h: Dict[TreeNode, int]) -> int:
        if root is None: return 0
        h[root] = 1+max(self.find_max_depth(root.left, h), self.find_max_depth(root.right, h))
        return h[root]