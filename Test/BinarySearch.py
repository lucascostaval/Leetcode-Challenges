from typing import List

# finds position of element in the array, if the element is not in the array return -1
def binary_search(lst: List[int], x: int) -> int:
    left, right = 0, len(lst)-1
    while left <= right:
        mid = left+(right-left)//2
        if x == lst[mid]: return mid
        elif x > lst[mid]: left = mid+1
        else: right = mid-1
    return -1

def binary_greater_or_equal_than(lst: List[int], x: int) -> int:
    left, right = 0, len(lst)-1
    while left <= right:
        mid = left+(right-left)//2
        if x == lst[mid]: return mid
        elif x > lst[mid]: left = mid+1
        else: right = mid-1
    return left

def binary_greater_than(lst: List[int], x: int) -> int:
    left, right = 0, len(lst)-1
    while left <= right:
        mid = left+(right-left)//2
        if x >= lst[mid]: left = mid+1
        else: right = mid-1
    return left

arr = [1, 2, 3, 5, 9, 13, 91]
x = 5
print(binary_search(arr, x))
print(binary_greater_or_equal_than(arr, x))
print(binary_greater_than(arr, x))