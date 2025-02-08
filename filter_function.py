ls = [1,2,3,4,5,6,7,8,9,10]
def filter_element(ls):
    return list(filter(lambda i:i%2==0, ls))
print(filter_element(ls))

word = ["ashish","ram","madhuri","sagar"]
def name_greater_than_4_latter(word):
    return list(filter(lambda latter:len(latter)>=5, word))
print(name_greater_than_4_latter(word))