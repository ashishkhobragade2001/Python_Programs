st = "aabbaaba"

def consicative_string(st):
    lists = []
    word = ""
    for i in st:
        if i == "a":
            word += i
        else:
            if len(word) >= 2:
                lists.append(word)
            word = ""
    # Append the last sequence if it meets the condition
    if len(word) >= 2:
        lists.append(word)
    if len(lists)>2:
        print("pass")
    else:
        print("fail")

consicative_string(st)
