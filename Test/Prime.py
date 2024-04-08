from typing import List, Dict

# Find out if a number is prime or not in O(n**(1/2)) time
def is_prime(x: int) -> bool:
    if x < 2: return False
    for i in range(2, int(x**0.5)+1):
        if x%i == 0: return False
    return True

# Returns list of all primes strictly less than n in O(nloglogn) time
def eratosthenes(n: int) -> List[int]:
    if n < 2: return []
    is_prime_lst: List[bool] = [True]*n
    for i in range(2, int(n**0.5)+1):
        for j in range(2*i, n, i): is_prime_lst[j] = False
    return [x for x in range(2, n) if is_prime_lst[x]]

def eratosthenes2(a: int, b: int) -> List[int]:
    if b < 2: return []
    is_prime_lst: List[bool] = [True]*b
    for i in range(2, int(b**0.5)+1):
        for j in range(2*i, b, i): is_prime_lst[j] = False
    return [x for x in range(min(a,2), b) if is_prime_lst[x]]

def decompose_into_primes(x: int) -> Dict[int, int]:
    result = {}
    i = 2
    while x > 1:
        if is_prime(i):
            if x%i == 0: result[i] = 0
            while x%i == 0:
                result[i] += 1
                x //= i
        i += 1
    return result

def decompose_into_unique_primes(x: int) -> List[int]:
    result = []
    i = 2
    while x > 1:
        if is_prime(i):
            if x%i == 0: result.append(i)
            while x%i == 0: x//= i
        i += 1
    return result

 
n = 100
print(eratosthenes(n))
print(decompose_into_primes(n))
print(decompose_into_unique_primes(n))