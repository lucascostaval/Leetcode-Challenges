from typing import List

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        isPrime: List[bool] = [True]*n
        for i in range(2, int(n**0.5)+1):
            for j in range(2*i, n, i): isPrime[j] = False
        result = 0
        for i in range(2, len(isPrime)):
            if isPrime[i]: result += 1
        return result


sol = Solution()
n = 18
print(sol.countPrimes(n))