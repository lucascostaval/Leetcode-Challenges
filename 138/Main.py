from typing import Dict, List, Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        h: Dict[Node, Node] = {}
        h[None] = None
        current: Node = head
        while current is not None: 
            h[current] = Node(current.val)
            current = current.next
        current = head
        while current is not None:
            h[current].next = h[current.next]
            h[current].random = h[current.random]
            current = current.next
        return h[head]
    

def array_to_ll(lst: List[int]):
    current = Node()
    tmp = current
    for x in lst:
        current.next = Node(x)
        current = current.next
    return tmp.next

def print_ll(head: Node):
    while head is not None:
        print("NEXT ELEMENT")
        print(head.val)
        if head.next is not None: print(head.next.val)
        if head.random is not None: print(head.random.val)
        print("\n\n")
        head = head.next

node1 = Node(7)
node2 = Node(13)
node3 = Node(11)
node4 = Node(10)
node5 = Node(1)
node1.next = node2
node1.random = None
node2.next = node3
node2.random = node1
node3.next = node4
node3.random = node5
node4.next = node5
node4.random = node3
node5.next = None
node5.random = node1
sol = Solution()
print_ll(sol.copyRandomList(node1))
