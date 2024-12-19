def length_of_longest_substring(s):
    char_index = {}
    left = max_length = 0
    
    for right, char in enumerate(s):
        if char in char_index:
            left = max(left, char_index[char] + 1)
        char_index[char] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length

s = "abcabcbb"
print("Length of longest substring:", length_of_longest_substring(s))
# Output: 3
