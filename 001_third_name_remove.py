st = "hello is ashish is my is name is khobragade "
remove = "is"
def third_name_remove(st, remove):
    words = st.split(" ")
    count = 0
    lists = []
    for word in words:
        if word == remove:
            count += 1
            if count == 3:
                lists.append("**")
                continue
            lists.append(word)
        else:
            lists.append(word)
    return " ".join(lists)
print(third_name_remove(st, remove))
