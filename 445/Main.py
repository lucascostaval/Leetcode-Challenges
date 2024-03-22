from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        result = ListNode()
        tmp = result
        cin = 0
        while l1 is not None and l2 is not None:
            s = (l1.val+l2.val+cin)%10
            cin = (l1.val+l2.val+cin)//10
            result.next = ListNode(s)
            result = result.next
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            s = (l1.val+cin)%10
            cin = (l1.val+cin)//10
            result.next = ListNode(s)
            result = result.next
            l1 = l1.next
        while l2 is not None:
            s = (l2.val+cin)%10
            cin = (l2.val+cin)//10
            result.next = ListNode(s)
            result = result.next
            l2 = l2.next
        if cin > 0: result.next = ListNode(cin)
        result = self.reverse(tmp.next)
        return result

    def reverse(self, head: ListNode) -> ListNode:
        before = None
        current = head
        after = head
        while current is not None:
            after = current.next
            current.next = before
            before = current
            current = after
        return before
    

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
arr1 = [5]
arr2 = [5]
head1 = make_ll_from_array(arr1)
head2 = make_ll_from_array(arr2)
result = sol.addTwoNumbers(head1, head2)
print_ll(result)