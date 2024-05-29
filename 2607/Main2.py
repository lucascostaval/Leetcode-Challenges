from typing import List

class Solution:

    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        gcd = self.euclid(len(arr), k)
        s = 0
        lst: List[List[int]] = [[] for _ in range(gcd)]
        for i in range(len(arr)): lst[i%gcd].append(arr[i])
        for l in lst:
            l.sort()
            middle_element = l[len(l)//2]
            for x in l: s += abs(x-middle_element)
        return s

    def euclid(self, a: int, b: int) -> int:
        while b != 0: a, b = b, a%b
        return a
    
    
sol = Solution()
arr = [2,5,5,7]
k = 3
print(sol.makeSubKSumEqual(arr, k))