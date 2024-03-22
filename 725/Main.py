from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        partitions: List[ListNode] = []
        for _ in range(k): partitions.append(ListNode())
        tmp: List[ListNode] = []
        for i in range(k): tmp.append(partitions[i])
        current = head
        length = self.get_length(head)
        in_each_house = length//k
        bonus_length_houses = length%k
        i = 0
        for i in range(bonus_length_houses):
            for _ in range(in_each_house+1):
                partitions[i].next = ListNode(current.val)
                partitions[i] = partitions[i].next
                current = current.next
        for i in range(bonus_length_houses, k):
            for j in range(in_each_house):
                partitions[i].next = ListNode(current.val)
                partitions[i] = partitions[i].next
                current = current.next
        for i in range(len(tmp)): tmp[i] = tmp[i].next
        return tmp
    
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
head = [1,2,3,4,5,6,7,8,9,10]
head = make_ll_from_array(head)
k = 3
result: List[ListNode] = sol.splitListToParts(head, k)
for x in result:
    print_ll(x)
    print("\n\n")
