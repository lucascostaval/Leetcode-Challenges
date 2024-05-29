from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        while i >= 0 and digits[i] == 9: i -= 1
        if i == -1: return [1]+[0]*len(digits)
        result: List[int] = []
        for k in range(i): result.append(digits[k])
        if i != -1: result.append(digits[i]+1)
        for k in range(i+1, len(digits)): result.append(0)
        return result


sol = Solution()
digits = [9, 8, 9, 9, 9]
print(sol.plusOne(digits))