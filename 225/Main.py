from collections import deque

class MyStack:

    def __init__(self):
        self.queue: deque = deque()
        self.size: int = 0

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.size += 1

    def pop(self) -> int:
        for _ in range(self.size-1):
            self.queue.append(self.queue.popleft())
        self.size -= 1
        return self.queue.popleft()

    def top(self) -> int:
        for _ in range(self.size-1):
            self.queue.append(self.queue.popleft())
        toPeek = self.queue.popleft()
        self.queue.append(toPeek)
        return toPeek
        
    def empty(self) -> bool:
        return self.size == 0


stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.top())
print(stack.push(4))
print(stack.pop())
print(stack.pop())
print(stack.top())
print(stack.pop())