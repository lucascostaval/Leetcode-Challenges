from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo: List[List[TreeNode]] = [[] for i in range(9)]
        memo[0] = [None]
        memo[1] = [TreeNode(1)]
        for m in range(2, 9):
            trees = []
            for rootValue in range(1, m+1):
                treesTemp = []
                for tree1 in memo[rootValue-1]:
                    for tree2 in memo[m-rootValue]:
                        tree = TreeNode(rootValue)
                        tree.left = self.cloneTree(tree1)
                        tree.right = self.cloneTree(tree2)
                        treesTemp.append(tree)
                for t in treesTemp:
                    self.traverseAndAdd(t.right, rootValue)
                    trees.append(t)
            memo[m] = trees
        return memo[n]

    def traverseAndAdd(self, node, valueToAdd):
        if node != None:
            self.traverseAndAdd(node.left, valueToAdd)
            node.val += valueToAdd
            self.traverseAndAdd(node.right, valueToAdd)

    def cloneTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        lst = []
        self.preorder(lst, root)
        treeRoot = TreeNode(lst[0])
        for i in range(1, len(lst)):
            self.insert(treeRoot, lst[i])
        return treeRoot

    def preorder(self, lst: List[int], node: TreeNode) -> None:
        if node != None:
            lst.append(node.val)
            self.preorder(lst, node.left)
            self.preorder(lst, node.right)

    def insert(self, root: TreeNode, x: int) -> None:
        isLeft = False
        parent = None
        current = root
        while current != None:
            parent = current
            if x <= current.val:
                current = current.left
                isLeft = True
            else:
                current = current.right
                isLeft = False
        toAdd = TreeNode(x)
        if isLeft:
            parent.left = toAdd
        else:
            parent.right = toAdd


sol = Solution()
sol.generateTrees(2)
