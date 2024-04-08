from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    INF = 100001

    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if head is None or head.next is None: return [-1, -1]
        first_critical_index: int = -1
        last_critical_index: int = -1
        node_1_index: int = -1
        node_2_index: int = -1
        before: ListNode = head
        current: ListNode = head.next
        after: ListNode = head.next.next
        minimum_distance = self.INF
        counter = 0
        while current.next is not None:
            counter += 1
            if (current.val > before.val and current.val > after.val) or (current.val < before.val and current.val < after.val):
                if first_critical_index == -1:
                    first_critical_index = counter
                    node_2_index = counter
                else:
                    node_1_index = node_2_index
                    node_2_index = counter
                    minimum_distance = min(minimum_distance, node_2_index-node_1_index)
                    last_critical_index = counter
            before = before.next
            current = current.next
            after = after.next
        maximum_distance = last_critical_index-first_critical_index
        if last_critical_index == -1: return [-1, -1]
        else: return [minimum_distance, maximum_distance]
            
            
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
head = [2, 2, 1, 3]
head = make_ll_from_array(head)
result = sol.nodesBetweenCriticalPoints(head)
print(result)