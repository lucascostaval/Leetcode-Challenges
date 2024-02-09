from typing import Optional

class TreeNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.previous, self.current = -100001, -100001
        self.minimum = 100000
        self.inorder(root)
        return self.minimum

    def inorder(self, root: TreeNode):
        if root is None:
            return
        self.inorder(root.left)
        self.current = root.val
        if self.current-self.previous <= self.minimum:
            self.minimum = self.current-self.previous
        self.previous = self.current
        self.inorder(root.right)