from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class QueueNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, x):
        new_node = QueueNode(x)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            removed: QueueNode = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return removed.val
        removed: QueueNode = self.head
        self.head = self.head.next
        self.length -= 1
        return removed.val
    
    def is_empty(self) -> bool:
        return self.length == 0

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None: return None
        queue = Queue()
        queue.add(node)
        visited = {node}
        copy_node = Node(node.val)
        h = {node: copy_node}
        while not queue.is_empty():
            removed_node = queue.pop()
            removed_copy_node = h[removed_node]
            for neighbor in removed_node.neighbors:
                if neighbor not in visited:
                    queue.add(neighbor)
                    visited.add(neighbor)
                if neighbor not in h.keys(): h[neighbor] = Node(neighbor.val)
                removed_copy_node.neighbors.append(h[neighbor])
        return copy_node
                

def print_graph(node: Node):
    if node is None: return None
    queue = Queue()
    queue.add(node)
    visited = set()
    visited.add(node)
    while not queue.is_empty():
        removed_node = queue.pop()
        for neighbor in removed_node.neighbors:
            print(f"({removed_node.val}: {neighbor.val})")
        for neighbor in removed_node.neighbors:
            if neighbor not in visited:
                queue.add(neighbor)
                visited.add(neighbor)

sol = Solution()
node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_1.neighbors = [node_2, node_4]
node_2.neighbors = [node_1, node_3]
node_3.neighbors = [node_2, node_4]
node_4.neighbors = [node_1, node_3]
copy_node_1 = sol.cloneGraph(node_1)
print_graph(node_1)
print("")
print_graph(copy_node_1)
print("")
print("Not same memory address" if node_1 is not copy_node_1 else "Same memory address")