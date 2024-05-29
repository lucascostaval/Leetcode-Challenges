from typing import List

class Solution:

    INF = 100000000000001

    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        gcd = self.euclid(len(arr), k)
        result = self.INF
        for a in range(1, gcd+1):
            if len(arr)%a == 0 and k%a == 0:
                s = 0
                lst: List[List[int]] = [[] for _ in range(a)]
                for i in range(len(arr)): lst[i%a].append(arr[i])
                for l in lst:
                    l.sort()
                    middle_element = l[len(l)//2]
                    for x in l: s += abs(x-middle_element)
                result = min(result, s)
        return result

    def euclid(self, a: int, b: int) -> int:
        while b != 0: a, b = b, a%b
        return a


sol = Solution()
arr = [2,5,5,7]
k = 3
print(sol.makeSubKSumEqual(arr, k))