def find_pairs(nums, target):
    seen = set()
    pairs = set()
    
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.add((min(num, complement), max(num, complement)))
        seen.add(num)
    
    return list(pairs)

nums = [1, 2, 3, 4, 3, 5]
target = 6
print("Pairs that sum to target:", find_pairs(nums, target))
# Output: [(1, 5), (2, 4), (3, 3)]
