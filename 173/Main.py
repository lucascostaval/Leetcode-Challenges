from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Pair:
    def __init__(self, node, state):
        self.node = node
        self.state = state

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
         self.stack = [Pair(root, 0)]

    def next(self) -> int:
        while True:
            pair = self.stack.pop()
            if pair.node is None:
                continue
            if pair.state == 0:
                self.stack.append(Pair(pair.node, 1))
                if pair.node.left is not None:
                    self.stack.append(Pair(pair.node.left, 0))
            elif pair.state == 1:
                x = pair.node.val
                if pair.node.right is not None:
                    self.stack.append(Pair(pair.node.right, 0))
                return x

    def hasNext(self) -> bool:
        return len(self.stack) > 0
    
root: TreeNode = TreeNode(7, TreeNode(3), TreeNode(15))
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)

bSTIterator = BSTIterator(root)
print(bSTIterator.next())    # return 3
print(bSTIterator.next())    # return 7
print(bSTIterator.hasNext()) # return True
print(bSTIterator.next())    # return 9
print(bSTIterator.hasNext()) # return True
print(bSTIterator.next())    # return 15
print(bSTIterator.hasNext()) # return True
print(bSTIterator.next())    # return 20
print(bSTIterator.hasNext()) # return False