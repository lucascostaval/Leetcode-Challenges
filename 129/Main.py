from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        lst: List[str] = self.get_numbers(root)
        s = 0
        for number in lst: s += int(number)
        return s

    def get_numbers(self, root: TreeNode) -> List[str]:
        if root is None: return []
        if root.left is None and root.right is None: return [str(root.val)]
        left_numbers = self.get_numbers(root.left)
        right_numbers = self.get_numbers(root.right)
        result: List[str] = []
        for number in left_numbers: result.append(str(root.val)+number)
        for number in right_numbers: result.append(str(root.val)+number)
        return result