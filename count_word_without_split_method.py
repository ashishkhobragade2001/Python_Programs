st = "asd kjh niuf as lkjhf lkjh"
def count_word(st):
    word = ""
    ls = []
    for char in st:
        if char != " ":
            word = word+char
        else:
            ls.append(word)
            word = ""
    ls.append(word)
    return ls
print(count_word(st))
print("Total no of word is :",len(count_word(st)))