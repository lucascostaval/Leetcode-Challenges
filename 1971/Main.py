from typing import List

class QueueNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.head: QueueNode = None
        self.tail: QueueNode = None
        self.length: int = 0

    def add(self, x: int) -> None:
        new_node = QueueNode(x)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self) -> int:
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
    
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}
        for i in range(n): graph[i] = []
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        queue = Queue()
        queue.add(source)
        visited = {source}
        while not queue.is_empty():
            removed_node = queue.pop()
            for neighbor in graph[removed_node]:
                if neighbor not in visited:
                    queue.add(neighbor)
                    visited.add(neighbor)
        return destination in visited
    

sol = Solution()
n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2
print(sol.validPath(n, edges, source, destination))