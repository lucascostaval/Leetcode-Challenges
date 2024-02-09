from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        currentSandwich = 0
        finished = False
        sandwiches.append(-1)
        while not finished:
            finished = True
            for i in range(len(students)):
                if students[i] == sandwiches[currentSandwich]:
                    currentSandwich += 1
                    students[i] = 2
                    finished = False
        return len(students)-currentSandwich
    
students = [1, 1, 0, 0]
sandwiches = [0, 1, 0, 1]
sol = Solution()
print(sol.countStudents(students, sandwiches))