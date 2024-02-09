from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        number_to_letters = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'],
                             ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        result = number_to_letters[int(digits[0])]
        for i in range(1, len(digits)):
            new_result = []
            for x in result:
                for y in number_to_letters[int(digits[i])]:
                    new_result.append(x+y)
            result = new_result
        return result


digits = "2345"
sol = Solution()
print(sol.letterCombinations(digits))
