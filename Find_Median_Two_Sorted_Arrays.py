def find_median_sorted_arrays(nums1, nums2):
    merged = sorted(nums1 + nums2)
    n = len(merged)
    mid = n // 2
    if n % 2 == 0:
        return (merged[mid - 1] + merged[mid]) / 2
    else:
        return merged[mid]

nums1 = [1, 3]
nums2 = [2]
print("Median:", find_median_sorted_arrays(nums1, nums2))
# Output: 2.0

