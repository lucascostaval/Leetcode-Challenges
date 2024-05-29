from typing import List

class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        primes: List[int] = self.eratosthenes(n+1)
        result: List[List[int]] = []
        left = 0
        right = len(primes)-1
        while left <= right:
            s = primes[left]+primes[right]
            if s == n: 
                result.append([primes[left], primes[right]])
                left += 1
                right -= 1
            elif s < n: left += 1
            else: right -= 1
        return result

    def eratosthenes(self, n: int) -> List[int]:
        if n < 2: return []
        is_prime = [True]*n
        for i in range(2, int(n**0.5)+1):
            for j in range(2*i, n, i): is_prime[j] = False
        return [x for x in range(2, n) if is_prime[x]]
    

sol = Solution()
n = 10
print(sol.findPrimePairs(n))