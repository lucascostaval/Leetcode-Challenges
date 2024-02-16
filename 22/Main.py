from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        characters = n*2
        result = []
        combinations = 1<<characters
        for b in range(combinations):
            s = ""
            i = 1
            while i < (combinations):
                if (b&i) == 0: s += "("
                else: s += ")"
                i *= 2
            if self.isValid(s): result.append(s)
        return result

    def isValid(self, s: str):
        count = 0
        for c in s:
            if c == "(": count += 1
            else: count -= 1
            if count < 0: return False
        return count == 0


sol = Solution()
n = 3
print(sol.generateParenthesis(n))