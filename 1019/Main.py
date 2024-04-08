from typing import List, Optional

class Pair:
    def __init__(self, first: int, second: int):
        self.first = first
        self.second = second

class StackNode:
    def __init__(self, val: Pair=None, next=None):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.head: StackNode = None
        self.tail: StackNode = None
        self.length: int = 0

    def add(self, x: Pair) -> None:
        new_node = StackNode(x)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop(self) -> Pair:
        if self.length == 0: return None
        if self.length == 1:
            removed = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return removed.val
        removed = self.head
        self.head = self.head.next
        self.length -= 1
        return removed.val
    
    def is_empty(self) -> bool:
        return self.length == 0

class ListNode:
    def __init__(self, val: int=0, next=None):
        self.val = val
        self.next = next

class Solution:

    INF = 1000000001

    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        length = self.get_length(head)
        result: List[int] = [0 for i in range(length)]
        lowest: int = self.INF
        stack: Stack = Stack()
        counter: int = 0
        while head is not None:
            if head.val > lowest:
                while True:
                    if stack.is_empty(): break
                    stack_item = stack.pop()
                    value = stack_item.first
                    index = stack_item.second
                    if head.val > value: result[index] = head.val
                    else:
                        stack.add(stack_item)
                        break
                lowest = head.val
            else: lowest = min(lowest, head.val)
            pair: Pair = Pair(head.val, counter)
            stack.add(pair)
            counter += 1
            head = head.next
        return result

    def get_length(self, head: ListNode) -> int:
        length = 0
        while head is not None:
            length += 1
            head = head.next
        return length


def print_ll(head: ListNode) -> None:
    print("Printing List!!!")
    while head is not None:
        print(head.val)
        head = head.next

def make_ll_from_array(lst: List[int]) -> ListNode:
    head = ListNode()
    tmp = head
    for x in lst:
        head.next = ListNode(x)
        head = head.next
    return tmp.next

sol = Solution()
head = [2,7,4,3,5]
head = make_ll_from_array(head)
result = sol.nextLargerNodes(head)
print(result)