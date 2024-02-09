from typing import Optional, List

class TreeNode:     
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.current_number = self.find_minimum(root)
        self.current_count = 0
        self.max_count = 0
        self.lst = []
        self.inorder(root)
        if self.current_count > self.max_count:
            self.lst = [self.current_number]
        elif self.current_count == self.max_count:
            self.lst.append(self.current_number)
        return self.lst

    def inorder(self, root: TreeNode) -> None:
        if root is None:
            return
        self.inorder(root.left)
        if root.val == self.current_number:
            self.current_count += 1
        else:
            if self.current_count > self.max_count:
                self.lst = [self.current_number]
                self.max_count = self.current_count
            elif self.current_count == self.max_count:
                self.lst.append(self.current_number)
            self.current_count = 1
            self.current_number = root.val
        self.inorder(root.right)

    def find_minimum(self, root: TreeNode):
        while root.left is not None:
            root = root.left
        return root.val


tree1: TreeNode = TreeNode(5, TreeNode(4), TreeNode(7))
tree1.left.left = TreeNode(3)
tree1.left.right = TreeNode(4)
tree1.right.left = TreeNode(5)
tree1.right.right = TreeNode(7)

tree2: TreeNode = TreeNode(1, None, TreeNode(2))
tree2.right.left = TreeNode(2)

tree3: TreeNode = TreeNode(0)

sol = Solution()
print(sol.findMode(tree1))
print(sol.findMode(tree2))
print(sol.findMode(tree3))