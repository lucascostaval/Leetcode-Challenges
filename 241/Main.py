from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        nums = []
        operations = []
        new_expression = ""
        for c in expression:
            if c in ('-', '+', '*'):
                operations.append(c)
                new_expression += ' '
            else:
                new_expression += c
        help_array = new_expression.split(' ')
        for x in help_array:
            nums.append(int(x))
        return self.compute(nums, operations)
    
    def compute(self, nums: List[int], operations: List[int]) -> List[int]:
        if len(nums) == 1: return nums
        result = []
        for i in range(len(operations)):
            left_part = self.compute(nums[0:i+1], operations[0:i])
            right_part = self.compute(nums[i+1:len(nums)], operations[i+1:len(operations)])
            for part1 in left_part:
                for part2 in right_part:
                    if operations[i] == '-': result.append(part1-part2)
                    elif operations[i] == '+': result.append(part1+part2)
                    elif operations[i] == '*': result.append(part1*part2)
        return result


sol = Solution()
expression = "2*3-4*5*12"
print(sol.diffWaysToCompute(expression))