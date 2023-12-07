from typing import Optional

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        before = None
        current = slow
        after = slow
        while current != None:
            after = current.next
            current.next = before
            before = current
            current = after
        while head != None and before != None:
            if head.val != before.val:
                return False
            head = head.next
            before = before.next
        return True