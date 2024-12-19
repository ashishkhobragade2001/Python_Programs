def group_anagrams(strs):
    anagrams = {}
    for s in strs:
        sorted_str = ''.join(sorted(s))
        anagrams.setdefault(sorted_str, []).append(s)
    return list(anagrams.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print("Grouped anagrams:", group_anagrams(strs))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
