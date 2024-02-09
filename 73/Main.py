from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        unique = 1
        found: bool = True
        while found:
            found = False
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == unique:
                        found = True
            unique += 1
        unique -= 1
        for i in range(len(matrix)):
            hasZero: bool = False
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    hasZero = True
            if hasZero:
                for j in range(len(matrix[0])):
                    if matrix[i][j] != 0: matrix[i][j] = unique
        for i in range(len(matrix[0])):
            hasZero: bool = False
            for j in range(len(matrix)):
                if matrix[j][i] == 0:
                    hasZero = True
            if hasZero:
                for j in range(len(matrix)):
                    if matrix[j][i] != 0: matrix[j][i] = unique
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == unique: matrix[i][j] = 0



sol = Solution()
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
sol.setZeroes(matrix)
print(matrix)