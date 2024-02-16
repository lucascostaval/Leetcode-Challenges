from typing import List

class Node:
    def __init__(self, val: chr, next=None):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.head: Node = None
    
    def add(self, x: chr) -> None:
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def pop(self) -> chr:
        if self.head is None: return None
        removed = self.head
        self.head = self.head.next
        return removed.val
    
    def peek(self) -> chr:
        if self.head is None: return None
        return self.head.val
    
    def empty(self) -> bool:
        return self.head is None

class Map:
    def __init__(self):
        self.arr = [[] for i in range(7)]

    def insert(self, key: chr, value: chr):
        k = ord(key)%len(self.arr)
        self.arr[k].append([key, value])

    def get(self, key) -> chr:
        k = ord(key)%len(self.arr)
        for pair in self.arr[k]:
            if pair[0] == key: return pair[1]
        return None
    
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.insert(key, value)

class Solution:
    def generateExpressions(self, characters: int) -> List[str]:
        lst = ['(', ')', '[', ']', '{', '}']
        result = []
        combinations = pow(6, characters)
        for b in range(combinations):
            s = ""
            i = 1
            current_number = b
            while i < combinations:
                x = current_number%6
                current_number //= 6
                i *= 6
                s += lst[x]
            if self.isValid(s): result.append(s)
        return result
    
    def isValid(self, s: str) -> bool:
        closing_to_opening = Map()
        opening = ('(', '[', '{')
        closing = (')', ']', '}')
        for i in range(len(opening)): closing_to_opening[closing[i]] = opening[i]
        stack = Stack()
        for c in s:
            if c in opening: stack.add(c)
            elif c in closing and stack.peek() == closing_to_opening[c]: stack.pop()
            else: return False
        return stack.empty()


sol = Solution()
n = 1
print(sol.generateExpressions(6))