class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def add(self, x) -> None:
        new_node = ListNode(x)
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
            removed = self.head.val
            self.head = None
            self.tail = None
            self.length = 0
            return removed
        removed = self.head.val
        self.head = self.head.next
        self.length -= 1
        return removed

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = Queue()
        self.h = {}
        self.size = 0
        
    def get(self, key: int) -> int:
        if key in self.h:
            return self.h[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if self.size == self.capacity:
            key_to_evict = self.queue.pop()
            self.h.pop(key_to_evict)
            self.size -= 1
        self.h[key] = value
        self.size += 1
        self.queue.add(key)

lruCache = LRUCache(2)
lruCache.put(1, 1)
lruCache.put(2, 2)
lruCache.get(1)
lruCache.put(3, 3)
lruCache.get(2)
lruCache.put(4, 4)
lruCache.get(1)
lruCache.get(3)
lruCache.get(4)