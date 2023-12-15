from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        lst = []
        while head != None:
            lst.append(head.val)
            head = head.next
        return self.create_tree(lst, 0, len(lst)-1)
    
    def create_tree(self, arr: List[int], left: int, right: int) -> TreeNode:
        if left > right:
            return None
        mid = left+(right-left)//2
        root = TreeNode(arr[mid])
        root.left = self.create_tree(arr, left, mid-1)
        root.right = self.create_tree(arr, mid+1, right)
        return root

def create_linked_list_by_array(arr: List[int]) -> ListNode:
    h = ListNode()
    tmp = h
    for x in arr:
        h.next = ListNode(x)
        h = h.next
    return tmp.next

def print_linked_list(h: ListNode) -> None:
    while h != None:
        print(h.val)
        h = h.next


arr = [1, 2, 3, 4, 5]
h = create_linked_list_by_array(arr)
sol = Solution()
result_tree = sol.sortedListToBST(h)