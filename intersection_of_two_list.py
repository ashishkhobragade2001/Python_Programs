def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

lst1 = [1, 2, 3, 4, 5]
lst2 = [3, 4, 5, 6, 7]
print("Intersection:", intersection(lst1, lst2))
# Output: [3, 4, 5]
