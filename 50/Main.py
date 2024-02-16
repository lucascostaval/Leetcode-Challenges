class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0: return 1/self.myPow(x, -n)
        if n == 0: return 1
        recursive_value = self.myPow(x, n//2)
        result = recursive_value*recursive_value
        if n%2 == 1: result = result*x
        return result


sol = Solution()
x = 2
n = -2
print(sol.myPow(x, n))