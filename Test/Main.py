from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = self.get_length(head)
        self._sortList(head, 0, length-1)
        return head

    def _sortList(self, head: ListNode, left: int, right: int) -> None:
        def partition(head, pivot_index, right):
            swap_index = pivot_index
            current: ListNode = head
            for _ in range(pivot_index): current = current.next
            iterator_node: ListNode = current.next
            pivot_node: ListNode = current
            swap_node: ListNode = current
            for _ in range(pivot_index+1, right+1):
                if iterator_node.val < pivot_node.val:
                    swap_node = swap_node.next
                    swap_node.val, iterator_node.val = iterator_node.val, swap_node.val
                    swap_index += 1
                iterator_node = iterator_node.next
            swap_node.val, pivot_node.val = pivot_node.val, swap_node.val
            return swap_index
        
        def best_of_three_pivot(head: ListNode, left: int, right: int) -> None:
            mid = (right+left)//2
            current: ListNode = head
            for _ in range(left): current = current.next
            left_node = current
            for _ in range(left, mid): current = current.next
            mid_node = current
            for _ in range(mid, right): current = current.next
            right_node = current
            if left_node.val > mid_node.val: left_node.val, mid_node.val = mid_node.val, left_node.val
            if mid_node.val > right_node.val: mid_node.val, right_node.val = right_node.val, mid_node.val
            if left_node.val > mid_node.val: left_node.val, mid_node.val = mid_node.val, left_node.val
            left_node.val, mid_node.val = mid_node.val, left_node.val

        if left > right: return
        best_of_three_pivot(head, left, right)
        pivot = partition(head, left, right)
        self._sortList(head, left, pivot-1)
        self._sortList(head, pivot+1, right)

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
head = [1, 2, 4, 2]
pre_lst = make_ll_from_array(head)
new_lst = sol.sortList(pre_lst)
print_ll(new_lst)