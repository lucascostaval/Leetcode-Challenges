from typing import List

class MaxHeap:
    def __init__(self):
        self.heap: List[int] = []
        self.length: int = 0

    def insert(self, x: int) -> None:
        self.heap.append(x)
        i = len(self.heap)-1
        while i > 0 and self.heap[i] > self.heap[(i-1)//2]:
            self.heap[i], self.heap[(i-1)//2] = self.heap[(i-1)//2], self.heap[i]
            i = (i-1)//2
    
    def remove(self) -> int:
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        removed = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sunk_down(0)
        return removed

    def sunk_down(self, index: int) -> None:
        max_index = index
        while True:
            left_index = 2*index+1
            right_index = 2*index+2
            if left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]: max_index = left_index
            if right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]: max_index = right_index
            if max_index == index: return
            self.heap[index], self.heap[max_index] = self.heap[max_index], self.heap[index]
            index = max_index


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = MaxHeap()
        for x in nums: heap.insert(x)
        for _ in range(k-1): heap.remove()
        return heap.remove()


nums = [3,2,3,1,2,4,5,5,6]
k = 4
sol = Solution()
print(sol.findKthLargest(nums, k))