from typing import List

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0
    
    def add(self, x: int):
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node
        self.length += 1

    def pop(self) -> int:
        if self.length == 0:
            return None
        removed = self.top
        self.top = self.top.next
        self.length -= 1
        return removed.val
    
    def peek(self) -> int:
        if self.length == 0:
            return None
        return self.top.val
    
    def is_empty(self) -> bool:
        return self.length == 0

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = Stack()
        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                stack.add(stack.peek()*2)
            elif op == "+":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.add(n2)
                stack.add(n1)
                stack.add(n1+n2)
            else:
                stack.add(int(op))
        result = 0
        while not stack.is_empty():
            result += stack.pop()
        return result


operations = ["5","2","C","D","+"]
sol = Solution()
result = sol.calPoints(operations)
print(result)