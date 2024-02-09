from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            if target-nums[i] in h: return [h[target-nums[i]], i]
            h[nums[i]] = i


sol = Solution()
nums = [2,7,11,15]
target = 9
print(sol.twoSum(nums, target))