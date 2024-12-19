def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

lst = [1, 3, 5, 7, 9, 11]
print("Index of 7:", binary_search(lst, 7))
# Output: 3
