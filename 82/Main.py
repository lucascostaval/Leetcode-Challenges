from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        currentValue = head.val
        counter = 0
        previous = None
        current = head
        helperNode = ListNode()
        tmp = helperNode
        while current != None:
            if current.val == currentValue:
                counter += 1
                previous = current
                current = current.next
            else:
                if counter == 1:
                    helperNode.next = previous
                    helperNode = helperNode.next
                currentValue = current.val
                counter = 0
        if counter == 1:
            helperNode.next = previous
            helperNode = helperNode.next
        return tmp.next

sol = Solution()
arr = [1,1,2]
h = ListNode()
tmp = h
for x in arr:
    h.next = ListNode(x)
    h = h.next
h = tmp.next
result = sol.deleteDuplicates(h)