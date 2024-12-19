import itertools
def find_all_permutation(st):
    ls = []
    lists = list(itertools.permutations(st))
    for i in lists:
        ls.append("".join(i))
    return ls  # Add return statement here

st = "abc"
print(find_all_permutation(st))
#['abc', 'acb', 'bac', 'bca', 'cab', 'cba']


def find_all_permutation(st):
    if len(st) == 0:
        return [""]
    
    permutations = []     
    for i in range(len(st)):
        current_char = st[i]
        remaining = st[:i] + st[i+1:]
        
        for i in find_all_permutation(remaining):
            permutations.append(current_char + i)
    
    return permutations

st = "ABC"
print(find_all_permutation(st))