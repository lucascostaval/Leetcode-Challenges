from typing import List

class Node:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.length: int = 0

    def add(self, x: int) -> None:
        new_node = Node(x)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self) -> int:
        if self.length == 0:
            return 10001
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
    
    def peek(self) -> int:
        if self.length == 0:
            return 10001
        return self.head.val
    
    def get_length(self) -> int:
        return self.length
    
    def is_empty(self) -> bool:
        return self.length == 0

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = Queue()
        dire = Queue()
        alive: List[bool] = [True]*len(senate)
        for i in range(len(senate)):
            if senate[i] == 'R':
                radiant.add(i)
            else:
                dire.add(i)
        while True:
            for i in range(len(senate)):
                party = senate[i]
                
                if radiant.is_empty():
                    return "Dire"
                elif dire.is_empty():
                    return "Radiant"
                
                if party == 'R' and alive[i]:
                    senator = dire.pop()
                    alive[senator] = False
                elif party == 'D' and alive[i]:
                    senator = radiant.pop()
                    alive[senator] = False

                if i == radiant.peek():
                    radiant.add(radiant.pop())
                elif i == dire.peek():
                    dire.add(dire.pop())



sol = Solution()
print(sol.predictPartyVictory("RDD"))