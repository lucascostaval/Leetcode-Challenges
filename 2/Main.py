from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        tmp = result
        c = 0
        while l1 is not None and l2 is not None:
            result.next = ListNode((l1.val+l2.val+c)%10)
            c = (l1.val+l2.val+c)//10
            result, l1, l2 = result.next, l1.next, l2.next
        while l1 is not None:
            result.next = ListNode((l1.val+c)%10)
            c = (l1.val+c)//10
            result, l1 = result.next, l1.next
        while l2 is not None:
            result.next = ListNode((l2.val+c)%10)
            c = (l2.val+c)//10
            result, l2 = result.next, l2.next
        if c != 0: result.next = ListNode(1)
        return tmp.next
    

def create_linked_list_by_array(arr: List[int]):
    result = ListNode()
    tmp = result
    for x in arr:
        result.next = ListNode(x)
        result = result.next
    return tmp.next

def print_linked_list(l: ListNode):
    while l is not None:
        print(l.val)
        l = l.next

sol = Solution()
l1 = create_linked_list_by_array([9,9,9,9,9,9,9])
l2 = create_linked_list_by_array([9,9,9,9])
print_linked_list(sol.addTwoNumbers(l1, l2))
