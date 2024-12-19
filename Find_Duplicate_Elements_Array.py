def find_duplicates(nums):
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    return list(duplicates)

nums = [1, 2, 3, 1, 2, 4]
print("Duplicates:", find_duplicates(nums))
# Output: [1, 2]
