from collections import Counter

def find_anagrams(s, p):
    p_count = Counter(p)
    s_count = Counter(s[:len(p) - 1])
    result = []

    for i in range(len(p) - 1, len(s)):
        s_count[s[i]] += 1  # Add current character
        if s_count == p_count:  # Compare counters
            result.append(i - len(p) + 1)
        s_count[s[i - len(p) + 1]] -= 1  # Remove the oldest character
        if s_count[s[i - len(p) + 1]] == 0:
            del s_count[s[i - len(p) + 1]]

    return result

s = "cbaebabacd"
p = "abc"
print("Anagram indices:", find_anagrams(s, p))
# Output: [0, 6]
