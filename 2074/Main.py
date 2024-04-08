from typing import List, Tuple, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: return head
        tmp = head
        groups: int = 1
        tail_1: ListNode = None
        tail_2: ListNode = head
        pre_head_2: ListNode = None
        after_tail_2: ListNode = None
        before: ListNode = head
        current: ListNode = head.next
        after: ListNode = head.next
        while current is not None:
            after = current.next
            pre_head_2: ListNode = before
            group_length = 1
            for _ in range(groups):
                before = current
                current = current.next
                if current is None: break
                after = after.next
                group_length += 1
            tail_1 = tail_2
            tail_2 = current if current is not None else before
            after_tail_2 = after
            if group_length%2 == 0:
                new_head, new_tail = self.reverse(tail_1.next, tail_2)
                pre_head_2.next = new_head
                new_tail.next = after_tail_2
                current = new_tail
                tail_2 = new_tail
            groups += 1
            if current is None: break
            before = current
            current = current.next
        return tmp

    def reverse(self, node_1: ListNode, node_2: ListNode) -> Tuple[ListNode, ListNode]:
        node_2.next = None
        before: ListNode = None
        current: ListNode = node_1
        after: ListNode = node_1
        while current is not None:
            after = current.next
            current.next = before
            before = current
            current = after
        return before, node_1


def make_ll_from_array(lst: List[int]) -> ListNode:
    head = ListNode()
    tmp = head
    for x in lst:
        head.next = ListNode(x)
        head = head.next
    return tmp.next

def print_ll(head: ListNode) -> None:
    print("Printing List")
    while head is not None:
        print(head.val)
        head = head.next


sol = Solution()
head = [1,1,0,6,5]
head = make_ll_from_array(head)
result = sol.reverseEvenLengthGroups(head)
print_ll(result)