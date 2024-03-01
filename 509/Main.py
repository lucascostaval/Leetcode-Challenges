from typing import List

class Solution:
    def fib(self, n: int) -> int:
        return self._fib(n, [-1]*31)

    def _fib(self, n, memo: List[int]) -> int:
        if n == 0 or n == 1: return n
        if memo[n] != -1: return memo[n]
        s = self._fib(n-1, memo)+self._fib(n-2, memo)
        memo[n] = s
        return memo[n]
    

sol = Solution()
print(sol.fib(30))