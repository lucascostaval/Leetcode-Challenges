from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs[0]) == 0: return ""
        s = ""
        current_index = 0
        while True:
            if current_index >= len(strs[0]):
                return s
            current_character = strs[0][current_index]
            for word in strs:
                if current_index >= len(word) or word[current_index] != current_character:
                    return s
            s += current_character
            current_index += 1