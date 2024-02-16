from typing import List, Tuple

class MinHeap:
    def __init__(self):
        self.heap: List[Tuple[int, int]] = []

    def insert(self, v1, v2) -> None:
        self.heap.append((v1, v2))
        index = len(self.heap)-1
        while index > 0 and (self.heap[index][0] < self.heap[(index-1)//2][0] or 
            (self.heap[index][0] == self.heap[(index-1)//2][0] and self.heap[index][1] < self.heap[(index-1)//2][1])):
            self.heap[index], self.heap[(index-1)//2] = self.heap[(index-1)//2], self.heap[index]
            index = (index-1)//2

    def remove(self) -> Tuple[int, int]:
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()
        removed = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sunk_down(0)
        return removed
    
    def sunk_down(self, index: int) -> None:
        min_index = index
        while True:
            left_index = index*2+1
            right_index = index*2+2
            if left_index < len(self.heap) and (self.heap[left_index][0] < self.heap[min_index][0] or 
                (self.heap[left_index][0] == self.heap[min_index][0] and self.heap[left_index][1] < self.heap[min_index][1])):
                min_index = left_index
            if right_index < len(self.heap) and (self.heap[right_index][0] < self.heap[min_index][0] or 
                (self.heap[right_index][0] == self.heap[min_index][0] and self.heap[right_index][1] < self.heap[min_index][1])):
                min_index = right_index
            if min_index == index: return
            self.heap[index], self.heap[min_index] = self.heap[min_index], self.heap[index]
            index = min_index

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = MinHeap()
        for i in range(len(mat)):
            power = sum(mat[i])
            heap.insert(power, i)
        result = []
        while k > 0:
            result.append(heap.remove()[1])
            k -= 1
        return result


sol = Solution()
mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
k = 3
print(sol.kWeakestRows(mat, k))