from typing import Dict, Tuple, Set, List

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        h: Dict[Tuple[int, int], int] = {}
        count = 0
        for rect in rectangles:
            reduced = self.reduce(rect[0], rect[1])
            if reduced in h: h[reduced] += 1
            else: h[reduced] = 1
        for v in list(h.values()): count += v*(v-1)//2
        return count
    
    def reduce(self, a: int, b: int) -> Tuple[int, int]:
        gcd: int = self.euclid(a, b)
        return (a//gcd, b//gcd)

    def euclid(self, a: int, b: int) -> int:
        while b != 0: a, b =  b, a%b
        return a


sol = Solution()
rectangles = [[4,5],[7,8]]
print(sol.interchangeableRectangles(rectangles))