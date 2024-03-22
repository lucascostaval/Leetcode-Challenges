from typing import List

def bubble_sort(lst: List[int]) -> None:
    for i in range(len(lst)-1):
        has_swap = False
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                has_swap = True
        if not has_swap: break

def selection_sort(lst: List[int]) -> None:
    for i in range(len(lst)-1):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]: min_index = j
        lst[min_index], lst[i] = lst[i], lst[min_index]

def insertion_sort(lst: List[int]) -> None:
    for i in range(1, len(lst)):
        current_number = lst[i]
        k = i-1
        while k >= 0 and lst[k] > current_number:
            lst[k+1] = lst[k]
            k -= 1
        lst[k+1] = current_number

def merge_sort(lst: List[int]) -> List[int]:
    def merge(lst1, lst2):
        result = []
        i, j = 0, 0
        while i < len(lst1) and j < len(lst2):
            if lst1[i] < lst2[j]:
                result.append(lst1[i])
                i += 1
            else:
                result.append(lst2[j])
                j += 1
        for k in range(i, len(lst1)): result.append(lst1[k])
        for k in range(j, len(lst2)): result.append(lst2[k])
        return result

    if len(lst) <= 1: return lst
    mid = len(lst)//2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def quick_sort(my_list):
    def pivot(my_list, pivot_index, end_index):
        swap_index = pivot_index
        for i in range(pivot_index+1, end_index+1):
            if my_list[i] < my_list[pivot_index]:
                swap_index += 1
                my_list[swap_index], my_list[i] = my_list[i], my_list[swap_index]
        my_list[swap_index], my_list[pivot_index] = my_list[pivot_index], my_list[swap_index]
        return swap_index

    def quick_sort_helper(my_list, left, right):
        if left >= right: return
        piv = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, piv-1)
        quick_sort_helper(my_list, piv+1, right)

    quick_sort_helper(my_list, 0, len(my_list)-1)

        

lst = [9, 3, 2, 991, 2, 4, 4, 2, 1, 8]
#bubble_sort(lst)
#selection_sort(lst)
lst = merge_sort(lst)
print(lst)