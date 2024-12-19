def are_rotations(s1, s2):
    if len(s1) != len(s2):
        return False
    return s1 in s2 + s2

s1 = "abcde"
s2 = "xvcdf"
print("Are rotations:", are_rotations(s1, s2))
# Output: True
