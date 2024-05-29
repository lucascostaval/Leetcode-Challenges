class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        while b != 0: a, b = b, a%b
        factors = 0
        for i in range(1, a+1):
            if a%i == 0: factors += 1
        return factors