from typing import List, Optional

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

    def __getitem__(self, x):
        current = self
        for _ in range(x): current = current.next
        return current

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        result = Node(0, None, None, None)
        tmp = result
        before = None
        while head is not None:
            result.next = head
            result = result.next
            before = result
            if head.child is not None:
                after = result.next
                sub_list = self.flatten(head.child)
                result.child = None
                result.next = sub_list
                result = result.next
                result.prev = before
                sub_list = sub_list.next
                while sub_list is not None:
                    result.next = sub_list
                    result = result.next
                    sub_list = sub_list.next
                # print("kdjawok")
                # print(result.val)
                # if result.next is not None: print(result.next.val)
                # if result.prev is not None: print(result.prev.val)
                result.next = after
                after.prev = result
                head = result
            head = head.next
        tmp = tmp.next
        if tmp is not None: tmp.prev = None
        return tmp


def make_ll_from_array(lst: List[int]) -> Node:
    head: Node = Node(0, None, None, None)
    before = None
    tmp = head
    for x in lst:
        head.next = Node(x, None, None, None)
        head.prev = before
        before = head
        head = head.next
    return tmp.next

def print_ll(head: Node) -> None:
    while head is not None:
        #print(head.val, head, head.next, head.prev, head.child)
        print("\nNew Node")
        print(head.val)
        if head.next is not None: print(head.next.val)
        if head.prev is not None: print(head.prev.val)
        head = head.next

sol = Solution()
arr = [1, 2, 3, 4, 5, 6]
head = make_ll_from_array(arr)
head[2].child = make_ll_from_array([7, 8, 9, 10])
head[2].child[1].child = make_ll_from_array([11, 12])
head = sol.flatten(head)
print_ll(head)