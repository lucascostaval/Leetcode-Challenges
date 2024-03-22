from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = self.get_length(head)
        beginning: ListNode = head
        ending: ListNode = head
        for _ in range(k-1): beginning = beginning.next
        for _ in range(length-k): ending = ending.next
        beginning.val, ending.val = ending.val, beginning.val
        return head
        
    def get_length(self, head: ListNode) -> int:
        length = 0
        while head is not None:
            length += 1
            head = head.next
        return length


def make_ll_from_array(lst: List[int]) -> ListNode:
    head = ListNode()
    tmp = head
    for x in lst:
        head.next = ListNode(x)
        head = head.next
    return tmp.next

def print_ll(head: ListNode) -> None:
    while head is not None:
        print(head.val)
        head = head.next

sol = Solution()
head = make_ll_from_array([7,9,6,6,7,8,3,0,9,5])
k = 5
head = sol.swapNodes(head, k)
print_ll(head)