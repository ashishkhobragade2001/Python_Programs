from collections import Counter

def are_anagrams(s1, s2):
    return Counter(s1) == Counter(s2)

s1 = "listen"
s2 = "silent"
print("Are anagrams:", are_anagrams(s1, s2))
# Output: True


def my_method(st1,st2):
    return sorted(st1)==sorted(st2)
print(my_method(s1,s2))