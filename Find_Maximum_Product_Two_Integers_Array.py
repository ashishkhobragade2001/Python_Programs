def max_product(nums):
    max1, max2 = float('-inf'), float('-inf')
    for num in nums:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    return max1 * max2

nums = [1, 5, 3, 9, 2]
print("Maximum product:", max_product(nums))
# Output: 45
