class MyCircularDeque:

    def __init__(self, k: int):
        self.max_size = k
        self.arr = [0]*k
        self.length = 0
        self.front = -1
        self.back = -1

    def insertFront(self, value: int) -> bool:
        if self.length == self.max_size:
            return False
        if self.length == 0:
            self.back = (self.back-1)%self.max_size
        self.front = (self.front-1)%self.max_size
        self.arr[self.front] = value
        self.length += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.length == self.max_size:
            return False
        if self.length == 0:
            self.front = (self.front+1)%self.max_size
        self.back = (self.back+1)%self.max_size
        self.arr[self.back] = value
        self.length += 1
        return True

    def deleteFront(self) -> bool:
        if self.length == 0:
            return False
        if self.length == 1:
            self.back = (self.back+1)%self.max_size
        self.front = (self.front+1)%self.max_size
        self.length -= 1
        return True

    def deleteLast(self) -> bool:
        if self.length == 0:
            return False
        if self.length == 1:
            self.front = (self.front-1)%self.max_size
        self.back = (self.back-1)%self.max_size
        self.length -= 1
        return True

    def getFront(self) -> int:
        if self.length == 0:
            return -1
        return self.arr[self.front]

    def getRear(self) -> int:
        if self.length == 0:
            return -1
        return self.arr[self.back]

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.max_size

myCircularDeque = MyCircularDeque(3)
myCircularDeque.insertLast(1);  # return True
myCircularDeque.insertLast(2);  # return True
myCircularDeque.insertFront(3); # return True
myCircularDeque.insertFront(4); # return False, the queue is full.
myCircularDeque.getRear();      # return 2
myCircularDeque.isFull();       # return True
myCircularDeque.deleteLast();   # return True
myCircularDeque.insertFront(4); # return True
myCircularDeque.getFront();     # return 4