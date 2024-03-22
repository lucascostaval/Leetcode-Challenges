from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: return head
        before = None
        current = head
        after = head
        while current is not None:
            after = current.next
            current.next = before
            before = current
            current = after
        tmp = before
        maximum_value = before.val
        current = before
        after = current
        after = current.next
        while after is not None:
            if after.val >= maximum_value:
                current.next = after
                current = after
                maximum_value = after.val
            after = after.next
        current.next = None
        before = None
        current = tmp
        after = tmp
        while current is not None:
            after = current.next
            current.next = before
            before = current
            current = after
        return before