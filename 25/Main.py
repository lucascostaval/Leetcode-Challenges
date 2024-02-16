from typing import Optional, List

class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        after = head
        last_from_group = None
        new_head = head
        while True:
            if not self.isValid(current, k): break
            current_head = current
            before = None
            for _ in range(k):
                after = current.next
                current.next = before
                before = current
                current = after
            if last_from_group is not None: last_from_group.next = before
            last_from_group = current_head
            if current_head == head: new_head = before
            last_from_group.next = current
        return new_head
    
    def isValid(self, current: ListNode, k: int) -> bool:
        length = 0
        while current is not None:
            current = current.next
            length += 1
        return length >= k
        

def array_to_ll(arr: List[int]):
    current = ListNode()
    tmp = current
    for x in arr:
        current.next = ListNode(x)
        current = current.next
    return tmp.next

def print_ll(h: ListNode):
    while h is not None:
        print(h.val)
        h = h.next

def reverse_ll(h: ListNode):
    before = None
    current = h
    after = h
    while current is not None:
        after = current.next
        current.next = before
        before = current
        current = after
    return before

arr = [1, 2, 3, 4, 5, 6, 7]
h = array_to_ll(arr)
sol = Solution()
new_h = sol.reverseKGroup(h, 2)
print_ll(new_h)

