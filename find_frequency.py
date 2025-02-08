from collections import Counter
ls = [1,1,2,3,1,2,2,3]

def frequency_find(ls):
    return {i:ls.count(i) for i in ls}
        
print("without any pre Define keyword :",frequency_find(ls))

def find_frequency(ls):
    return dict(Counter(ls))
    
print("using Counter method :",find_frequency(ls))