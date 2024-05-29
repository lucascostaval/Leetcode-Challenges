from typing import List

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        primes = self.eratosthenes(1001)
        x = -1
        for n in nums:
            minimum_required = x+1
            if n < minimum_required: return False
            remove_threshold = n-minimum_required
            if remove_threshold != n: remove_threshold += 1
            p = self.lesser(primes, remove_threshold)
            x = n-p
        return True
    
    def lesser(self, lst: List[int], x: int) -> int:
        left, right = 0, len(lst)-1
        while left <= right:
            mid = left+(right-left)//2
            if x > lst[mid]: left = mid+1
            else: right = mid-1
        if right == -1: return 0
        return lst[right]

    def eratosthenes(self, n: int) -> List[int]:
        if n < 2: return []
        is_prime = [True]*n
        for i in range(2, int(n**0.5)+1):
            for j in range(2*i, n, i): is_prime[j] = False
        return [x for x in range(2, n) if is_prime[x]]


sol = Solution()
nums = [5,8,3]
print(sol.primeSubOperation(nums))