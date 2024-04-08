from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result: ListNode = ListNode()
        tmp = result
        current: ListNode = head.next
        s: int = 0
        while current is not None:
            if current.val == 0:
                result.next = ListNode(s)
                result = result.next
                s = 0
            else: s += current.val
            current = current.next
        return tmp.next