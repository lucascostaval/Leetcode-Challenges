from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        list1: ListNode = ListNode()
        list2: ListNode = ListNode()
        tmp1: ListNode = list1
        tmp2: ListNode = list2
        current = head
        while current != None:
            if current.val < x:
                list1.next = ListNode(current.val)
                list1 = list1.next
            else:
                list2.next = ListNode(current.val)
                list2 = list2.next
            current = current.next
        list1.next = tmp2.next
        return tmp1.next

def create_list_by_array(arr: List[int]) -> ListNode:
    h = ListNode()
    tmp = h
    for x in arr:
        h.next = ListNode(x)
        h = h.next
    return tmp.next

def print_list(lst: ListNode) -> None:
    current = lst
    while current != None:
        print(current.val)
        current = current.next

lst1 = [1, 2, 4, 9, 3]
h = create_list_by_array(lst1)
sol = Solution()
result: ListNode = sol.partition(h, 4)
print_list(result)