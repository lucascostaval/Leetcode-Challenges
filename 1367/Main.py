from typing import List, Dict, Tuple, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        current = self
        result = []
        while current is not None:
            result.append(current.val)
            current = current.next
        return str(result)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        print("=================")
        print(self.val)
        if self.left is not None: print(self.left.val)
        if self.right is not None: print(self.right.val)
        print("=================")

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        return self._isSubPath(head, head, root, {})
    
    def _isSubPath(self, original_head: ListNode, head: ListNode, root: TreeNode, memo: Dict[Tuple[ListNode, TreeNode], bool]) -> bool:
        if head is None: return True
        if root is None: return False
        if (head, root) in memo: return memo[(head, root)]
        tmp = head
        if root.val == head.val: head = head.next
        else: head = original_head
        value = (self._isSubPath(original_head, head, root.left, memo) or
                 self._isSubPath(original_head, head, root.right, memo) or
                 self._isSubPath(original_head, original_head, root.left, memo) or
                 self._isSubPath(original_head, original_head, root.right, memo))
        memo[(tmp, root)] = value
        return memo[(tmp, root)]
    

def make_ll_from_array(lst: List[int]) -> ListNode:

    head: ListNode = ListNode()
    tmp = head
    for x in lst:
        head.next = ListNode(x)
        head = head.next
    return tmp.next

sol = Solution()
# head = [4, 2, 8]
# head = make_ll_from_array(head)
# root = TreeNode(1, TreeNode(4), TreeNode(4))
# root.left.right = TreeNode(2, TreeNode(1))
# root.right.left = TreeNode(2, TreeNode(6), TreeNode(8))
# root.right.left.right.left = TreeNode(1)
# root.right.left.right.right = TreeNode(3)
head = [1, 10]
head = make_ll_from_array(head)
root = TreeNode(1, None, TreeNode(1, TreeNode(10, TreeNode(9)), TreeNode(1)))
print(sol.isSubPath(head, root))