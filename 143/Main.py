from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return
        lst = []
        while head != None:
            lst.append(head)
            head = head.next
        left = 0
        right = len(lst)-1
        while left < right:
            if right != left+1:
                lst[right].next = lst[left+1]
            lst[left].next = lst[right]
            left += 1
            right -= 1
        lst[left].next = None
    
def make_linked_list_from_array(arr: List[int]):
    h = ListNode()
    tmp = h
    for x in arr:
        h.next = ListNode(x)
        h = h.next
    return tmp.next

def print_linked_list(head: ListNode):
    while head != None:
        print(head.val)
        head = head.next

arr = [1, 2, 3, 4, 5, 6, 7]
sol = Solution()
h = make_linked_list_from_array(arr)
sol.reorderList(h)
print_linked_list(h)
