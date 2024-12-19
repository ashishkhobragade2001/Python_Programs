import re

def is_palindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return s == s[::-1]

s = "A man, a plan, a canal: Panama"
print("Is palindrome:", is_palindrome(s))
# Output: True
