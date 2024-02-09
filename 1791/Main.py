from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        s = set()
        for edge in edges:
            if edge[0] in s: return edge[0]
            if edge[1] in s: return edge[1]
            s.add(edge[0])
            s.add(edge[1])
        return -1