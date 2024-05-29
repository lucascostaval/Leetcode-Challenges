from typing import List

class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        minimum = min(nums)
        can_not_divide: bool = False
        for x in nums:
            if x%minimum != 0: can_not_divide = True
        if can_not_divide: return 1
        count = 0
        for x in nums:
            if x == minimum: count += 1
        return (count+1)//2

sol = Solution()
nums = [5,2,2,2,9,10]
print(sol.minimumArrayLength(nums))