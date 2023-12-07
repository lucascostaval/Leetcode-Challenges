from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        length: int = self.get_length(head)
        preLeft: ListNode = self.get(head, left-2, length)
        leftNode: ListNode = self.get(head, left-1, length)
        rightNode: ListNode = self.get(head, right-1, length)
        posRight: ListNode = self.get(head, right, length)
        
        before = None
        current = leftNode
        after = leftNode
        while current != posRight:
            after = current.next
            current.next = before
            before = current
            current = after
        if preLeft != None:
            preLeft.next = rightNode
        leftNode.next = posRight
        if left == 1:
            head = rightNode
        return head

    def get(self, head: ListNode, index: int, length: int) -> ListNode:
        if index < 0 or index >= length:
            return None
        current = head
        for _ in range(index):
            current = current.next
        return current

    def get_length(self, head):
        current: ListNode = head
        tot = 0
        while current != None:
            current = current.next
            tot += 1
        return tot
    
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

arr = [1, 2, 3, 4, 5]
h = create_list_by_array(arr)
sol = Solution()
h = sol.reverseBetween(h, 1, 5)
print_list(h)