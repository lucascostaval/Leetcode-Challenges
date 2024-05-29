class Solution:
    def smallestValue(self, n: int) -> int:
        last_n = n
        while True: 
            n = self.add_primes_decomposed(n)
            if n == last_n: break
            last_n = n
        return n

    def add_primes_decomposed(self, n: int) -> int:
        result = 0
        i = 2
        while n > 1:
            if n%i == 0 and self.is_prime(i):
                while n%i == 0:
                    result += i
                    n //= i
            i += 1
        return result

    def is_prime(self, x: int) -> bool:
        if x < 2: return False
        for i in range(2, int(x**0.5)+1):
            if x%i == 0: return False
        return True
    
sol = Solution()
n = 4
print(sol.smallestValue(n))