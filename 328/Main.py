from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        tail = head
        while tail.next != None:
            tail = tail.next
        tmp = tail
        previous = head
        current = head.next
        while previous != tmp and previous != tmp.next:
            if tmp.next != None:
                print(tmp.next.val)
            print(previous.val, current.val)
            tail.next = current
            tail = tail.next
            previous.next = current.next
            current.next = None
            previous = previous.next
            current = previous.next
        return head

sol = Solution()
arr = [1,2,3,4,5,6]
h = ListNode()
tmp = h
for x in arr:
    h.next = ListNode(x)
    h = h.next
h = tmp.next
result = sol.oddEvenList(h)