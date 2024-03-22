from typing import List, Dict, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        queue1: Queue = Queue()
        queue1.add(self)
        result: List[int] = []
        while not queue1.is_empty():
            queue2: Queue = Queue()
            while not queue1.is_empty():
                node: TreeNode = queue1.pop()
                result.append(node.val) if node is not None else result.append(None)
                if node is not None:
                    queue2.add(node.left)
                    queue2.add(node.right)
            while not queue2.is_empty(): queue1.add(queue2.pop())
        return str(result)       

class QueueNode:
    def __init__(self, val: TreeNode, next=None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.head: QueueNode = None
        self.tail: QueueNode = None
        self.length: int = 0

    def add(self, x: TreeNode) -> None:
        new_node = QueueNode(x)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self) -> TreeNode:
        if self.length == 0: return None
        if self.length == 1:
            removed: TreeNode = self.head.val
            self.head = None
            self.tail = None
            self.length = 0
            return removed
        removed: TreeNode = self.head.val
        self.head = self.head.next
        self.length -= 1
        return removed
    
    def is_empty(self) -> bool:
        return self.length == 0
    
    def __len__(self) -> int:
        return self.length

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        return self._allPossibleFBT(n, {})

    def _allPossibleFBT(self, n: int, h: Dict[int, TreeNode]) -> List[Optional[TreeNode]]:
        if n == 0: return []
        if n == 1: return [TreeNode(0)]
        if n in h: return h[n]
        result: List[TreeNode] = []
        for i in range(n):
            for tree_left in self._allPossibleFBT(i, h):
                for tree_right in self._allPossibleFBT(n-1-i, h):
                    root = TreeNode(0)
                    root.left = tree_left
                    root.right = tree_right
                    if self.isFull(root): result.append(root)
        h[n] = result
        return h[n]

    def isFull(self, tree: TreeNode) -> bool:
        if tree is None: return True
        if tree.right is None and tree.left is not None or tree.right is not None and tree.left is None: return False
        return self.isFull(tree.left) and self.isFull(tree.right)
    

sol = Solution()
n = 9
trees = sol.allPossibleFBT(n)
for tree in trees: print(tree)