def longest_palindromic_substring(s):
    res = ""
    
    def expand_around_center(left, right):
        nonlocal res
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > len(res):
                res = s[left:right + 1]
            left -= 1
            right += 1

    for i in range(len(s)):
        expand_around_center(i, i)  # Odd length
        expand_around_center(i, i + 1)  # Even length

    return res

s = "babad"
print("Longest palindromic substring:", longest_palindromic_substring(s))
# Output: "bab" or "aba"
