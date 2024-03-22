from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(lst1: ListNode, lst2: ListNode):
            result = ListNode()
            tmp = result
            while lst1 is not None and lst2 is not None:
                if lst1.val < lst2.val:
                    result.next = ListNode(lst1.val)
                    lst1 = lst1.next
                else:
                    result.next = ListNode(lst2.val)
                    lst2 = lst2.next
                result = result.next
            while lst1 is not None:
                result.next = ListNode(lst1.val)
                result = result.next
                lst1 = lst1.next
            while lst2 is not None:
                result.next = ListNode(lst2.val)
                result = result.next
                lst2 = lst2.next
            return tmp.next

        if head is None or head.next is None: return head
        length = self.get_length(head)
        lst1 = ListNode()
        lst2 = ListNode()
        tmp1, tmp2 = lst1, lst2
        mid = length//2
        current = head
        for _ in range(mid):
            lst1.next = ListNode(current.val)
            lst1 = lst1.next
            current = current.next
        for _ in range(mid, length):
            lst2.next = ListNode(current.val)
            lst2 = lst2.next
            current = current.next
        lst1 = self.sortList(tmp1.next)
        lst2 = self.sortList(tmp2.next)
        return merge(lst1, lst2)
    
    def get_length(self, head: ListNode):
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
arr = []
head = make_ll_from_array(arr)
head = sol.sortList(head)
print_ll(head)