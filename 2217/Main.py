from typing import List

class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        lst = []
        palindromes = self.getPalindromes(intLength)
        print(len(palindromes))
        for x in queries:
            if x > len(palindromes):
                lst.append(-1)
            else:
                lst.append(int(palindromes[x-1]))
        return lst

    def getPalindromes(self, size, startIndex=1):
        #print("Recursive Call")
        if size == 1:
            lst = []
            for i in range(startIndex, 10):
                lst.append(str(i))
            return lst
        if size == 2:
            lst = []
            for i in range(startIndex, 10):
                c = str(i)
                lst.append(c+c)
            return lst
        lst = []
        s = ""
        palindromes = self.getPalindromes(size-2, 0)
        for i in range(startIndex, 10):
            for palindrome in palindromes:
                s = str(i)+palindrome+str(i)
                lst.append(s)
        print(f"finished with size {size}")
        print(f"length of lst: {len(lst)}")
        return lst
            

        

arr = [572521748,377073593,2,43160372,987707952,6,391690915,56,85]
length = 13
sol = Solution()
print(sol.kthPalindrome(arr, length))