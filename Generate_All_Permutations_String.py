from itertools import permutations

def all_permutations(s):
    return [''.join(p) for p in permutations(s)]

s = "abc"
print("Permutations:", all_permutations(s))
# Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
