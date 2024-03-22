from typing import Optional
from random import randint

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.length = self.calculate_length(self.head)

    def getRandom(self) -> int:
        k = randint(0, self.length-1)
        current: ListNode = self.head
        for _ in range(k): current = current.next
        return current.val

    def calculate_length(self, head):
        length = 0
        while head is not None:
            length += 1
            head = head.next
        return length