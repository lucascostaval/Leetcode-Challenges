from typing import List

class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        primes: List[int] = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                number = str(mat[i][j])
                for current_j in range(j+1, len(mat[0])):
                    number += str(mat[i][current_j])
                    if self.is_prime(int(number)): primes.append(int(number))
                number = str(mat[i][j])
                current_i = i
                current_j = j
                while current_i+1 < len(mat) and current_j+1 < len(mat[0]):
                    current_i += 1
                    current_j += 1
                    number += str(mat[current_i][current_j])
                    if self.is_prime(int(number)): primes.append(int(number))
                number = str(mat[i][j])
                for current_i in range(i+1, len(mat)):
                    number += str(mat[current_i][j])
                    if self.is_prime(int(number)): primes.append(int(number))
                number = str(mat[i][j])
                current_i = i
                current_j = j
                while current_i+1 < len(mat) and current_j-1 >= 0:
                    current_i += 1
                    current_j -= 1
                    number += str(mat[current_i][current_j])
                    if self.is_prime(int(number)): primes.append(int(number))
                number = str(mat[i][j])
                for current_j in range(j-1, -1, -1):
                    number += str(mat[i][current_j])
                    if self.is_prime(int(number)): primes.append(int(number))
                number = str(mat[i][j])
                current_i = i
                current_j = j
                while current_i-1 >= 0 and current_j-1 >= 0:
                    current_i -= 1
                    current_j -= 1
                    number += str(mat[current_i][current_j])
                    if self.is_prime(int(number)): primes.append(int(number))
                number = str(mat[i][j])
                for current_i in range(i-1, -1, -1):
                    number += str(mat[current_i][j])
                    if self.is_prime(int(number)): primes.append(int(number))
                number = str(mat[i][j])
                current_i = i
                current_j = j
                while current_i-1 >= 0 and current_j+1 < len(mat[0]):
                    current_i -= 1
                    current_j += 1
                    number += str(mat[current_i][current_j])
                    if self.is_prime(int(number)): primes.append(int(number))
        h = {}
        for p in primes:
            if p in h: h[p] += 1
            else: h[p] = 1
        most_common_prime = -1
        most_times_appeared = -1
        for k, v in h.items():
            if v > most_times_appeared or v == most_times_appeared and k > most_common_prime:
                most_common_prime = k
                most_times_appeared = v
        return most_common_prime          

    def is_prime(self, x: int) -> bool:
        if x < 2: return False
        for i in range(2, int(x**0.5)+1):
            if x%i == 0: return False
        return True


sol = Solution()
mat = [[1,2,6],[7,9,8]]
print(sol.mostFrequentPrime(mat))