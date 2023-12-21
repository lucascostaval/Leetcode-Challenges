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
    def evalRPN(self, tokens: List[str]) -> int:
        stack = Stack()
        for token in tokens:
            if token == "+":
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                stack.add(n1+n2)
            elif token == "-":
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                stack.add(n1-n2)
            elif token == "*":
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                stack.add(n1*n2)
            elif token == "/":
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                negative = n1*n2 < 0
                stack.add(abs(n1)//abs(n2)*negative)
            else:
                stack.add(int(token))
        return stack.pop()


tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
sol = Solution()
result = sol.evalRPN(tokens)
print(result)