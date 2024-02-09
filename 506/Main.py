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
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        h = {}
        result = [""]*len(score)
        for i in range(len(score)): h[score[i]] = i
        heap = MaxHeap()
        for x in score: heap.insert(x)
        if len(score) > 0: result[h[heap.remove()]] = "Gold Medal"
        if len(score) > 1: result[h[heap.remove()]] = "Silver Medal"
        if len(score) > 2: result[h[heap.remove()]] = "Bronze Medal"
        for i in range(len(score)-3): result[h[heap.remove()]] = str(i+4)
        return result


score = [10,3,8,9,4]
sol = Solution()
print(sol.findRelativeRanks(score))