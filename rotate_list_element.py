def rotate(lst, steps):
    steps %= len(lst)
    return lst[-steps:] + lst[:-steps]

lst = [1, 2, 3, 4, 5]
steps = 2
print("Rotated list:", rotate(lst, steps))
# Output: [4, 5, 1, 2, 3]
