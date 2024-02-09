class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.length: int = 0

    def add(self, x: int) -> None:
        new_node = Node(x)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self) -> int:
        if self.length == 0:
            return -1
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
    
    def peek(self) -> int:
        if self.length == 0:
            return -1
        return self.head.val
    
    def get_length(self) -> int:
        return self.length

class RecentCounter:
    def __init__(self):
        self.queue = Queue()

    def ping(self, t: int) -> int:
        self.queue.add(t)
        minimum_time = t-3000
        while self.queue.peek() < minimum_time:
            self.queue.pop()
        return self.queue.get_length()


counter = RecentCounter()
print(counter.ping(1))
print(counter.ping(100))
print(counter.ping(3001))
print(counter.ping(3002))