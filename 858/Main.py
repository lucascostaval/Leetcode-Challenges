class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        right = True
        d = 0
        direction = 1
        while True:
            d += q*direction
            if d == 0: return 0
            if d == p:
                if right: return 1
                else: return 2
            if d > p or d < 0: direction *= -1
            if d > p: d = p-(d-p)
            elif d < 0: d = -d
            right = not right


sol = Solution()
p = 10
q = 3
print(sol.mirrorReflection(p, q))