from collections import Counter

def most_frequent_elements(lst):
    freq = Counter(lst)
    max_freq = max(freq.values())
    return [k for k, v in freq.items() if v == max_freq]

lst = [1, 3, 3, 2, 1, 1, 2, 4, 4, 4]
print("Most frequent elements:", most_frequent_elements(lst))
# Output: [1, 4] if both appear equally frequently
