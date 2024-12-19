def has_all_unique_chars(s):
    if len(s) > 128:  # Assuming ASCII
        return False
    char_set = [False] * 128
    for char in s:
        index = ord(char)
        if char_set[index]:
            return False
        char_set[index] = True
    return True

s = "abcdefg"
print("All unique characters:", has_all_unique_chars(s))
# Output: True

def my_method(st):
    di = {i:st.count(i) for i in st}
    for k,v in di.items():
        if v>=2:
            return False
    return True
st = "asdfghjkl"
print("All unique characters:",my_method(st))
