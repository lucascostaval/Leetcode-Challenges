class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n != 1:
            s.add(n)
            new_n = 0
            for c in str(n):
                new_n += int(c)*int(c)
            if new_n in s:
                return False
            n = new_n
        return True