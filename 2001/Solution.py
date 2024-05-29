from typing import Dict, Tuple, List

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        h: Dict[Tuple[int, int]] = {}
        count = 0
        for rect in rectangles:
            a, b = rect[0], rect[1]
            while b != 0: a, b = b, a%b
            reduced_w, reduced_h = rect[0]//a, rect[1]//a
            if (reduced_w, reduced_h) in h: 
                count += h[(reduced_w, reduced_h)]
                h[(reduced_w, reduced_h)] += 1
            else: h[(reduced_w, reduced_h)] = 1
        return count