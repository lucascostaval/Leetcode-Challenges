from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for x in nums: s.add(x)
        return len(s) < len(nums)


sol = Solution()
nums = [1, 2, 3, 1]
print(sol.containsDuplicated(nums))