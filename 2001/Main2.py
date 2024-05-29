from typing import Dict, List

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        h: Dict[float, int] = {}
        for rect in rectangles:
            value = rect[0]/rect[1]
            if value in h: h[value] += 1
            else: h[value] = 1
        count = 0
        for v in list(h.values()): count += v*(v-1)//2
        return count