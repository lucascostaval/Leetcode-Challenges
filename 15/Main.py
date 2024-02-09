from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_set = set()
        for i in range(len(nums)):
            h = {}
            for j in range(i+1, len(nums)):
                if 0-(nums[i]+nums[j]) in h:
                    arr = [nums[i], nums[j], 0-(nums[i]+nums[j])]
                    arr.sort()
                    result_set.add((arr[0], arr[1], arr[2]))
                h[nums[j]] = j
        result: List[List[int]] = []
        for tuple in result_set: result.append(list(tuple))
        return result


sol = Solution()
nums = [0,0,0]
print(sol.threeSum(nums))