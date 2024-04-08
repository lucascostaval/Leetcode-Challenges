from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow: ListNode = head
        fast: ListNode = head
        while fast is not None:
            slow = slow.next
            fast = fast.next.next
        before = None
        current = slow
        after = slow
        while current is not None:
            after = current.next
            current.next = before
            before = current
            current = after
        max_sum = -1
        while before is not None:
            max_sum = max(max_sum, head.val+before.val)
            head = head.next
            before = before.next
        return max_sum


def make_ll_from_array(lst: List[int]):
    head = ListNode()
    tmp = head
    for x in lst:
        head.next = ListNode(x)
        head = head.next
    return tmp.next


sol = Solution()
head = [5,4,2,1]
head = make_ll_from_array(head)
print(sol.pairSum(head))