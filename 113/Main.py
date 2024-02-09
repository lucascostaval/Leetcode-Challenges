from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val    
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result: List[List[int]] = []
        current_path: List[int] = []
        self.pathSumHelper(root, targetSum, current_path, result)
        return result

    def pathSumHelper(self, root: TreeNode, targetSum: int, current_path: List[int], result: List[List[int]]) -> None:
        if root is None:
            return
        current_path.append(root.val)
        self.pathSumHelper(root.left, targetSum-root.val, current_path, result)
        if root.left is None and root.right is None:
            if root.val == targetSum:
                result.append(current_path.copy())
        self.pathSumHelper(root.right, targetSum-root.val, current_path, result)
        current_path.pop()


root: TreeNode = TreeNode(5, TreeNode(4), TreeNode(8))
root.left.left = TreeNode(11, TreeNode(7), TreeNode(2))
root.right.left = TreeNode(13)
root.right.right = TreeNode(4, TreeNode(5), TreeNode(1))
sol = Solution()
print(sol.pathSum(root, 22))