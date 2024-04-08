from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: return None
        before_slow: ListNode = None
        slow: ListNode = head
        fast: ListNode = head
        while fast is not None and fast.next is not None:
            before_slow = slow
            slow = slow.next
            fast = fast.next.next
        before_slow.next = slow.next
        return head
