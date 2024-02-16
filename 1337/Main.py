from typing import List, Dict

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, x: int) -> None:
        self.heap.append(x)
        index = len(self.heap)-1
        while index > 0 and self.heap[index] < self.heap[(index-1)//2]:
            self.heap[index], self.heap[(index-1)//2] = self.heap[(index-1)//2], self.heap[index]
            index = (index-1)//2

    def remove(self) -> int:
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
            if left_index < len(self.heap) and self.heap[left_index] < self.heap[min_index]: min_index = left_index
            if right_index < len(self.heap) and self.heap[right_index] < self.heap[min_index]: min_index = right_index
            if index == min_index: return
            self.heap[index], self.heap[min_index] = self.heap[min_index], self.heap[index]
            index = min_index

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        h: Dict[int, List[int]] = {}
        heap = MinHeap()
        for i in range(len(mat)):
            power = sum(mat[i])
            if power in h: h[power].append(i)
            else: 
                h[power] = [i]
                heap.insert(power)
        result = []
        while k > 0:
            for x in h[heap.remove()]:
                result.append(x)
                k -= 1
                if k <= 0: break
        return result


sol = Solution()
mat = [[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]]
k = 2
print(sol.kWeakestRows(mat, k))