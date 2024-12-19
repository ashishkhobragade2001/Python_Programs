def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

st1 = "ashish"
st2 = "shiash"
print(are_anagrams(st1,st2))
# Output: True
