st= "Hello"
#output = "Holle"
def reverse_of_string(st):
    first_latter = st[0]
    word = st[1::]
    rev = word[::-1]
    return first_latter+rev
print(reverse_of_string(st))    #"Holle"