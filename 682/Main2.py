from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                stack.append(stack[len(stack)-1]*2)
            elif op == "+":
                stack.append(stack[len(stack)-1]+stack[len(stack)-2])
            else:
                stack.append(int(op))
        return sum(stack)


operations = ["5","2","C","D","+"]
sol = Solution()
result = sol.calPoints(operations)
print(result)