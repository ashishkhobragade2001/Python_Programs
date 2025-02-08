from functools import reduce
ls = [1,2,3,4,5]
def product_of_element(ls):
    return reduce(lambda x,y:x*y, ls)
print(product_of_element(ls))

a=1
def proct_element(ls):
    global a 
    for i in ls:
        a= a*i
    return a
print(proct_element(ls))