from typing import List

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, x: int) -> None:
        self.heap.append(x)
        index = len(self.heap)-1
        while index > 0 and self.heap[index] > self.heap[(index-1)//2]:
            self.heap[index], self.heap[(index-1)//2] = self.heap[(index-1)//2], self.heap[index]
            index = (index-1)//2

    def remove(self) -> int:
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()
        removed = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sunk_down(0)
        return removed

    def sunk_down(self, index) -> None:
        max_index = index
        while True:
            left_index = 2*index+1
            right_index = 2*index+2
            if left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]: max_index = left_index
            if right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]: max_index = right_index
            if index == max_index: return
            self.heap[index], self.heap[max_index] = self.heap[max_index], self.heap[index]
            index = max_index

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = MaxHeap()
        for x in stones: heap.insert(x)
        n = len(stones)
        while n > 1:
            stone_1 = heap.remove()
            stone_2 = heap.remove()
            if stone_1 == stone_2:
                n -= 2
            else:
                n -= 1
                heap.insert(stone_1-stone_2)
        if n == 0: return 0
        return heap.remove()



sol = Solution()
stones = [2,7,4,1,8,1]
print(sol.lastStoneWeight(stones))