class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        result_arr = []
        current_index = 0
        while current_index < len(s):
            result_arr.append(s[current_index])
            current_index += 2*numRows-2
        for i in range(1, numRows-1):
            current_index = i
            while current_index < len(s):
                result_arr.append(s[current_index])
                current_index += 2*numRows-2-2*i
                if current_index < len(s): result_arr.append(s[current_index])
                current_index += 2*i
        current_index = numRows-1
        while current_index < len(s):
            result_arr.append(s[current_index])
            current_index += 2*numRows-2
        return "".join(result_arr)


sol = Solution()
s = "PAYPALISHIRING"
numRows = 1
print(sol.convert(s, numRows))