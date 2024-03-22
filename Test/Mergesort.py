from typing import List

def merge_sort(lst: List[int]) -> List[int]:
    def merge(lst1: List[int], lst2: List[int]):
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
    
    if len(lst) == 1: return lst
    mid = len(lst)//2
    lst1 = merge_sort(lst[:mid])
    lst2 = merge_sort(lst[mid:])
    return merge(lst1, lst2)


lst = [4, 2, 1, 3]
lst_sorted = merge_sort(lst)
print(lst_sorted)