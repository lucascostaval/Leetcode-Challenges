from typing import List

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                first, last = int(str(nums[i])[0]), int(str(nums[j])[len(str(nums[j]))-1])  
                while last != 0: first, last = last, first%last
                if first == 1: count += 1
        return count


sol = Solution()
nums = [11,21,12]
print(sol.countBeautifulPairs(nums))