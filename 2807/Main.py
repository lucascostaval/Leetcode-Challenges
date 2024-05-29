from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous: ListNode = head
        current: ListNode = head.next
        while current is not None:
            gcd = self.euclid(previous.val, current.val)
            previous.next = ListNode(gcd, current)
            previous = current
            current = current.next
        return head

    def euclid(self, a: int, b: int) -> int:
        while b != 0: a, b = b, a%b
        return a
    

def make_ll_from_arr(lst: List[int]) -> ListNode:
    current = ListNode()
    tmp = current
    for x in lst:
        current.next = ListNode(x)
        current = current.next
    return tmp.next

def print_ll(head: ListNode) -> None:
    while head is not None:
        print(head.val)
        head = head.next


sol = Solution()
head = [7]
head = make_ll_from_arr(head)
result = sol.insertGreatestCommonDivisors(head)
print_ll(result)