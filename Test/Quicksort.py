def quick_sort(lst) -> None:
    _quick_sort(lst, 0, len(lst)-1)
    
def _quick_sort(lst, left, right) -> None:
    def partition(lst, partition_index, right):
        swap_index = partition_index
        for i in range(partition_index+1, right+1):
            if lst[i] < lst[partition_index]:
                swap_index += 1
                lst[i], lst[swap_index] = lst[swap_index], lst[i]
        lst[swap_index], lst[partition_index] = lst[partition_index], lst[swap_index]
        return swap_index
    
    def best_of_tree_pivot(lst, left, right):
        mid = (right+left)//2
        if lst[left] > lst[mid]: lst[left], lst[mid] = lst[mid], lst[left]
        if lst[mid] > lst[right]: lst[mid], lst[right] = lst[right], lst[mid]
        if lst[left] > lst[mid]: lst[left], lst[mid] = lst[mid], lst[left]
        lst[left], lst[mid] = lst[mid], lst[left]

    if left > right: return
    best_of_tree_pivot(lst, left, right)
    pivot = partition(lst, left, right)
    _quick_sort(lst, left, pivot-1)
    _quick_sort(lst, pivot+1, right)


lst = [2, 3, 1]
print(len(lst))
quick_sort(lst)
print(lst)