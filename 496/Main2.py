from typing import List

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.head: Node = None
        self.length = 0
    
    def add(self, x: int) -> None:
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
    
    def pop(self) -> int:
        if self.length == 0:
            return None
        if self.length == 1:
            removed = self.head
            self.head = None
            self.length = 0
            return removed.val
        removed = self.head
        self.head = self.head.next
        self.length -= 1
        return removed.val

    def peek(self) -> int:
        if self.length == 0:
            return None
        return self.head.val
    
    def is_empty(self):
        return self.length == 0

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h = {}
        stack = Stack()
        stack.add(nums2[0])
        for i in range(1, len(nums2)):
            while not stack.is_empty() and stack.peek() < nums2[i]:
                h[stack.pop()] = nums2[i]
            stack.add(nums2[i])
        while not stack.is_empty():
            h[stack.pop()] = -1
        result = []
        for x in nums1:
            result.append(h[x])
        return result
    
sol = Solution()
arr1 = [2,4]
arr2 = [1,2,3,4]
result = sol.nextGreaterElement(arr1, arr2)
print(result)