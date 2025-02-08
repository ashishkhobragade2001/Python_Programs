st = "python is a programming language"
def longest_word(st):
    
    def split_word(st):
        ls = []
        word = ""
        for i in st:
            if i != " ":
                word = word+i
            else:
                ls.append(word)
                word = ""
        ls.append(word)
        return ls
    ## one method    
    ls = split_word(st)
    #return max(ls, key=len)
    
    ## onather method 
    di = {}
    for word in ls:
        total_latter = len(word)
        di[total_latter]=word
    
    max_k = max(di)
    return di[max_k]
    
print(longest_word(st))
                
