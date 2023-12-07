from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        tail = head
        length = 0
        while tail.next != None:
            tail = tail.next
            length += 1
        length += 1
        newTailIndex = length-(k%length)
        tail.next = head
        previous = tail
        current = head
        for _ in range(newTailIndex):
            previous = previous.next
            current = current.next
        previous.next = None
        return current

sol = Solution()
arr = [1,2,3,4,5]
h = ListNode()
tmp = h
for x in arr:
    h.next = ListNode(x)
    h = h.next
h = tmp.next
result = sol.rotateRight(h, 2)