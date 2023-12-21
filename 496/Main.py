from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h = {}
        stack = [nums2[0]]
        for i in range(1, len(nums2)):
            while len(stack) != 0 and stack[len(stack)-1] < nums2[i]:
                h[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        while len(stack) > 0:
            h[stack.pop()] = -1
        result = []
        for x in nums1:
            result.append(h[x])
        return result


sol = Solution()
arr1 = [2,4]
arr2 = [1,2,3,4]
result = sol.nextGreaterElement(arr1, arr2)
print(result)