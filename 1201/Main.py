class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        left = 1
        right = 2000000000
        lcm_ab = self.lcm(a, b)
        lcm_ac = self.lcm(a, c)
        lcm_bc = self.lcm(b, c)
        lcm_abc = self.lcm(self.lcm(a, b), c)
        while left <= right:
            mid = left+(right-left)//2
            multiples_a = (mid-1)//a
            multiples_b = (mid-1)//b
            multiples_c = (mid-1)//c
            multiples_ab = (mid-1)//lcm_ab
            multiples_ac = (mid-1)//lcm_ac
            multiples_bc = (mid-1)//lcm_bc
            multiples_abc = (mid-1)//lcm_abc
            multiples_before = multiples_a+multiples_b+multiples_c-multiples_ab-multiples_bc-multiples_ac+multiples_abc
            if multiples_before == n-1 and (mid%a == 0 or mid%b == 0 or mid%c == 0): return mid
            elif multiples_before > n-1: right = mid-1
            else: left = mid+1

    def lcm(self, a: int, b: int) -> int:
        gcd = self.euclid(a, b)
        return a*b//gcd
    
    def euclid(self, a: int, b: int) -> int:
        while b != 0: a, b = b, a%b
        return a


sol = Solution()
n, a, b, c = 5, 2, 11, 13
print(sol.nthUglyNumber(n, a, b, c))