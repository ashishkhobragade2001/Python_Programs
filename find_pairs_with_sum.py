def find_pairs_with_sum(lst, target):
    pairs = []
    seen = set()
    for num in lst:
        complement = target - num
        if complement in seen:
            pairs.append((min(num, complement), max(num, complement)))
        seen.add(num)
    return list(set(pairs))

lst = [1, 2, 3, 4, 3, 5]
target = 6
print("Pairs with sum 6:", find_pairs_with_sum(lst, target))
# Output: [(1, 5), (2, 4), (3, 3)]
