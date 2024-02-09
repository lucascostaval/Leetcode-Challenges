from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        h = {}
        for i in range(1, n+1): h[i] = []
        for t in trust: h[t[0]].append(t[1])
        judge = -1
        for person in h.keys():
            if h[person] == []:
                judge = person
                break
        for person in h.keys(): 
            if person != judge and judge not in h[person]: return -1
        return judge
    

sol = Solution()
n = 3
trust = [[1,3],[2,3]]
print(sol.findJudge(n, trust))