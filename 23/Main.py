from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next = next

class QueueNode:
    def __init__(self, val, next=None):
        self.val: ListNode = val
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def add(self, llnode: ListNode):
        new_node = QueueNode(llnode)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self) -> ListNode:
        if self.length == 0:
            return None
        if self.length == 1:
            removed = self.head.val
            self.head = None
            self.tail = None
            self.length = 0
            return removed
        removed = self.head.val
        self.head = self.head.next
        self.length -= 1
        return removed
    
    def get_length(self) -> int:
        return self.length
    
    def is_empty(self) -> bool:
        return self.length == 0
    
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        queue1: Queue = Queue()
        queue2: Queue = Queue()
        for list in lists:
            queue1.add(list)
        k = queue1.get_length()
        while k > 1:
            while k >= 2:
                l1 = queue1.pop()
                l2 = queue1.pop()
                merged_list = self.mergeLists(l1, l2)
                queue2.add(merged_list)
                k = queue1.get_length()
            if not queue1.is_empty():
                queue2.add(queue1.pop())
            new_k = queue2.get_length()
            for _ in range(new_k):
                queue1.add(queue2.pop())
            k = queue1.get_length()
        result = queue1.pop()
        return result

    def mergeLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        result = ListNode()
        tmp = result
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                result.next = list1
                list1 = list1.next
            else:
                result.next = list2
                list2 = list2.next
            result = result.next
        while list1 != None:
            result.next = list1
            result = result.next
            list1 = list1.next
        while list2 != None:
            result.next = list2
            result = result.next
            list2 = list2.next
        return tmp.next
    

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

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
ll_lists: List[ListNode] = [create_list_by_array(x) for x in lists]
sol = Solution()
result: ListNode = sol.mergeKLists(ll_lists)
print_list(result)