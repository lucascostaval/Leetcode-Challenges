class Solution:
    def lastRemaining(self, n: int) -> int:
        left = 1
        right = n
        jump_length = 1
        i = 0
        while n > 1:
            if i%2 == 0:
                left += jump_length
                if n%2 != 0: right -= jump_length
            else:
                right -= jump_length
                if n%2 != 0: left += jump_length
            jump_length *= 2
            n //= 2
            i += 1
        return left


sol = Solution()
n = 9
print(sol.lastRemaining(100))