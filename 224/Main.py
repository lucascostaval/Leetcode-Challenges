class Solution:
    def calculate(self, s: str) -> int:
        formated_string_builder = []
        for c in s:
            if c != " ":
                formated_string_builder.append(c)
        formated_string = "".join(formated_string_builder)
        return self._calculate(formated_string)
    
    def _calculate(self, s: str) -> int:
        i = 0
        total = 0
        number_string = ""
        operation = "+"
        digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        operations = {"+", "-"}
        while i < len(s):
            symbol = s[i]
            if symbol in digits: number_string += symbol
            elif symbol in operations:
                if number_string == "": operation = symbol
                else:
                    if operation == "+": total += int(number_string)
                    elif operation == "-": total -= int(number_string)
                    operation = symbol
                    number_string = ""
            elif symbol == "(":
                i += 1
                inner_expression_builder = []
                open_count = 1
                while True:
                    if s[i] == '(': open_count += 1
                    elif s[i] == ')': open_count -= 1
                    if open_count <= 0: break
                    inner_expression_builder.append(s[i])
                    i += 1
                inner_expression = "".join(inner_expression_builder)
                number_string = str(self._calculate(inner_expression))
            i += 1
        if operation == "+": total += int(number_string)
        elif operation == "-": total -= int(number_string)
        return total