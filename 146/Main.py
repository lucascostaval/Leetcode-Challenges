from typing import Dict

class Node:
    def __init__(self, val: int, next=None):
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
        if self.length == 0: return None
        if self.length == 1:
            removed: Node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return removed.val
        removed: Node = self.head
        self.head = self.head.next
        self.length -= 1
        return removed.val

class LRUCache:

    def __init__(self, capacity: int):
        self.queue = Queue()
        self.capacity: int = capacity
        self.size: int = 0
        self.key_to_times: Dict[int, int] = {}
        self.key_to_value: Dict[int, int] = {}
        

    def get(self, key: int) -> int:
        if key in self.key_to_value:
            self.queue.add(key)
            self.key_to_times[key] += 1
            return self.key_to_value[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_value:
            self.key_to_value[key] = value
            self.queue.add(key)
            self.key_to_times[key] += 1
            return
        if self.size == self.capacity:
            while True:
                queue_item = self.queue.pop()
                if self.key_to_times[queue_item] > 0: self.key_to_times[queue_item] -= 1
                else:
                    del self.key_to_times[queue_item]
                    del self.key_to_value[queue_item]
                    break
            self.size -= 1
        if key in self.key_to_value: self.key_to_times[key] += 1
        else: self.key_to_times[key] = 0
        self.key_to_value[key] = value
        self.size += 1
        self.queue.add(key)