from typing import List, Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        slow: ListNode = head
        fast: ListNode = head.next
        cycle_node: ListNode = None
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                cycle_node = slow
                break
        if cycle_node is None: return None
        s = set()
        current = cycle_node
        while current not in s:
            s.add(current)
            current = current.next
        while not head in s: head = head.next
        return head
    

def array_to_ll(lst: List[int]):
    current = ListNode(0)
    tmp = current
    for x in lst:
        current.next = ListNode(x)
        current = current.next
    return tmp.next

sol = Solution()
arr = [1, 2]
head = array_to_ll(arr)
head.next.next = head
output = sol.detectCycle(head)
if output is not None: print(output.val)