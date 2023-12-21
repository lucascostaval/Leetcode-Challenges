class Solution:
    def simplifyPath(self, path: str) -> str:
        path_after_procedure = ""
        for i in range(len(path)-1):
            if path[i] == '/' and path[i+1] == '/':
                continue
            path_after_procedure += path[i]
        if path[len(path)-1] != '/':
            path_after_procedure += path[len(path)-1]
        path_after_procedure = path_after_procedure[1::]
        path_after_procedure += '/'
        stack = []
        directory = ""
        for i in range(len(path_after_procedure)):
            if path_after_procedure[i] == '/':
                if directory == ".." and len(stack) > 0:
                    stack.pop()
                elif directory != ".." and directory != ".":
                    stack.append(directory)
                directory = ""
            else:
                directory += path_after_procedure[i]
        result = ""
        for i in range(len(stack)):
            result = result + '/' + stack[i]
        if result == "":
            result += '/'
        return result
        

s = "///TJbrd/owxdG//"
sol = Solution()
simplified_string = sol.simplifyPath(s)
print(simplified_string)