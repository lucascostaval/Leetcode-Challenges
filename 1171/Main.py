from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        change_status = True
        before_iterator_1: ListNode = None
        while change_status:
            change_status = False
            iterator_1 = head
            while iterator_1 is not None:
                s = 0
                iterator_2 = iterator_1
                while iterator_2 is not None:
                    after_iterator_2: ListNode = iterator_2.next
                    s += iterator_2.val
                    if s == 0:
                        change_status = True
                        s = 0
                        if before_iterator_1 is None: head = after_iterator_2
                        else: before_iterator_1.next = after_iterator_2
                    if change_status: break
                    iterator_2 = iterator_2.next
                if change_status: break
                before_iterator_1 = iterator_1
                iterator_1 = iterator_1.next
        return head
                        

def print_ll(head: ListNode) -> None:
    print("Printing List!!!")
    while head is not None:
        print(head.val)
        head = head.next

def make_ll_from_array(lst: List[int]) -> ListNode:
    head = ListNode()
    tmp = head
    for x in lst:
        head.next = ListNode(x)
        head = head.next
    return tmp.next

sol = Solution()
head = [1,2,3,-3,-2]
head = make_ll_from_array(head)
result = sol.removeZeroSumSublists(head)
print_ll(result)