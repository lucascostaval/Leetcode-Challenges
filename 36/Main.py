from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s1, s2 = set(), set()
            for j in range(9):
                if board[i][j] in s1 or board[j][i] in s2: return False
                if board[i][j] != '.': s1.add(board[i][j])
                if board[j][i] != '.': s2.add(board[j][i])
        lst = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] in lst[i//3][j//3]: return False
                if board[i][j] != '.': lst[i//3][j//3].add(board[i][j])
        return True
                

sol = Solution()
board =[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(sol.isValidSudoku(board))