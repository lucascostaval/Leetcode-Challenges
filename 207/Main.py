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
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses): graph[i] = set()
        for edge in prerequisites: graph[edge[0]].add(edge[1])
        queue = Queue()
        visited = set()
        for v in graph.keys():
            if len(graph[v]) == 0:
                queue.add(v)
                visited.add(v)
        while not queue.is_empty():
            removed_node = queue.pop()
            for v in graph.keys():
                if removed_node in graph[v]:
                    graph[v].remove(removed_node)
                if len(graph[v]) == 0 and v not in visited:
                    queue.add(v)
                    visited.add(v)
        return sum(visited)==numCourses*(numCourses-1)/2


sol = Solution()
numCourses = 2
prerequisites = [[1,0],[0,1]]
print(sol.canFinish(numCourses, prerequisites))