from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        tmp = list1
        after_cut = list1
        for _ in range(b+1): after_cut = after_cut.next
        for _ in range(a-1): list1 = list1.next
        list1.next = list2
        tail_list2 = list2
        while tail_list2.next is not None: tail_list2 = tail_list2.next
        tail_list2.next = after_cut
        return tmp
    
def print_ll(head: ListNode) -> None:
    print("Printing List")
    while head is not None:
        print(head.val)
        head = head.next

def make_ll_from_arr(arr: List[int]) -> ListNode:
    head = ListNode()
    tmp = head
    for x in arr:
        head.next = ListNode(x)
        head = head.next
    return tmp.next
    

sol = Solution()
head1 = [10,1,13,6,9,5]
a = 3
b = 4
head2 = [1000000,1000001,1000002]
head1 = make_ll_from_arr(head1)
head2 = make_ll_from_arr(head2)
result = sol.mergeInBetween(head1, a, b, head2)
print_ll(result)
