class QueueNode:
    def __init__(self, val: 'Node', next=None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, x: 'Node'):
        new_node = QueueNode(x)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self) -> 'Node':
        if self.length == 0:
            return None
        if self.length == 1:
            removed = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return removed.val
        removed = self.head
        self.head = self.head.next
        self.length -= 1
        return removed.val
    
    def is_empty(self) -> bool:
        return self.length == 0

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue: Queue = Queue()
        if root is not None: queue.add(root)
        while not queue.is_empty():
            helper_queue: Queue = Queue()
            previous = None
            current = queue.pop()
            if current.left is not None: helper_queue.add(current.left)
            if current.right is not None: helper_queue.add(current.right)
            while not queue.is_empty():
                previous = current               
                current = queue.pop()
                previous.next = current
                if current.left is not None: helper_queue.add(current.left)
                if current.right is not None: helper_queue.add(current.right)
            while not helper_queue.is_empty():
                queue.add(helper_queue.pop())
        return root


tree = Node(1, Node(2), Node(3))
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.right.right = Node(7)
sol = Solution()
sol.connect(tree)
print("done")
