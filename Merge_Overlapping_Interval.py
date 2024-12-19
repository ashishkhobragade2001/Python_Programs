def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for i in intervals[1:]:
        if i[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], i[1])
        else:
            merged.append(i)
    return merged

intervals = [[1, 3], [2, 4], [5, 7], [6, 8]]
print("Merged intervals:", merge_intervals(intervals))
# Output: [[1, 4], [5, 8]]
