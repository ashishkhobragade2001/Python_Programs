ls = ["ketki", "rahul", "ashwarya"]

def second_character_replace_by_symbol(ls):
    main_list = []
    for word in ls:
        counts = {}  
        new_word = []
        for char in word:
            if char in counts:
                counts[char] += 1
                if counts[char] == 2:  
                    new_word.append("$")
                else:
                    new_word.append(char)
            else:
                counts[char] = 1
                new_word.append(char)
        main_list.append("".join(new_word))
    return main_list

print(second_character_replace_by_symbol(ls))
