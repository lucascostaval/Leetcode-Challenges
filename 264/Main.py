class Solution:
    def nthUglyNumber(self, n: int) -> int:
        max_integer = 2123366400
        lst = []
        a = 1
        while True:
            b = 1
            while True:
                c = 1
                while True:
                    if a*b*c > max_integer: break
                    lst.append(a*b*c)
                    c *= 2
                b *= 3
                if a*b > max_integer: break
            if a > max_integer: break
            a *= 5
        lst.sort()
        return lst[n-1]


sol = Solution()
n = 1690
print(sol.nthUglyNumber(n))
