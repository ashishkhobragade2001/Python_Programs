from collections import defaultdict

def group_by_first_char(words):
    grouped = defaultdict(list)
    for word in words:
        grouped[word[0]].append(word)
    return dict(grouped)

words = ["apple", "banana", "apricot", "blueberry", "cherry"]
print("Grouped by first character:", group_by_first_char(words))
# Output: {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}
