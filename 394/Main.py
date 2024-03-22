class Solution:
    def decodeString(self, s: str) -> str:
        number_string = ""
        i = 0
        digits = {str(i) for i in range(10)}
        result = ""
        while i < len(s):
            c = s[i]
            if c in digits: number_string += c
            elif c == "[":
                sub_string = ""
                brackets_count = 1
                while True:
                    i += 1
                    if s[i] == '[': brackets_count += 1
                    elif s[i] == ']': brackets_count -= 1
                    if brackets_count == 0: break
                    sub_string += s[i]
                sub_string_result = self.decodeString(sub_string)
                repetitions = int(number_string)
                number_string = ""
                for _ in range(repetitions): result += sub_string_result
            else: result += c
            i += 1
        return result