ls = [1,1,1,1,2,2,3]
def most_common_element(ls):
    di = {ls.count(i):i for i in ls}
    max_k = max(di.keys())
    return di[max_k]
print(most_common_element(ls))