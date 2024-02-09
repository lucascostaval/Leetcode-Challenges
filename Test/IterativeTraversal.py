from typing import Optional, List

class Pair:
    def __init__(self, node, state):
        self.node = node
        self.state = state

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            if node is not None:
                lst.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return lst
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        lst = []
        stack = [Pair(root, 0)]
        while len(stack) > 0:
            pair = stack.pop()
            if pair.node is None:
                continue
            if pair.state == 0:
                stack.append(Pair(pair.node, 1))
                stack.append(Pair(pair.node.left, 0))
            elif pair.state == 1:
                lst.append(pair.node.val)
                stack.append(Pair(pair.node.right, 0))
        return lst


root = TreeNode(1, None, TreeNode(2))
root.right.left = TreeNode(3)
sol = Solution()
lst = sol.inorderTraversal(root)
print(lst)