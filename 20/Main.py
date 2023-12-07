class Stack:

    def __init__(self, maxSize: int = 0):
        self.arr = [' ' for i in range(maxSize)]
        self.top = -1

    def add(self, c: chr) -> None:
        self.top += 1
        self.arr[self.top] = c

    def pop(self) -> chr:
        c = self.arr[self.top]
        self.top -= 1
        return c
    
    def peek(self, offset: int = 0) -> chr:
        return self.arr[self.top-offset]
    
    def empty(self):
        return self.top == -1


class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack(maxSize=len(s))
        endChar = {')': '(', ']': '[', '}': '{'}
        for c in s:
            stack.add(c)
            if c in (')', ']', '}') and stack.peek(offset=1) == endChar[c]:
                stack.pop()
                stack.pop()
        return stack.empty()

    
class Main:
    def main(self):
        s = "({}[([])])"
        solution = Solution()
        result = solution.isValid(s)
        print(result)


def run():
    mainObj = Main()
    mainObj.main()

if __name__ == "__main__":
    run()