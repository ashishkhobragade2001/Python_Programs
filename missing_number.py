ls = [1,2,3,5,6]
def misssing_number(ls):
    expected_sum = sum(range(min(ls),max(ls)+1))
    actual_sum = sum(ls)
    return expected_sum - actual_sum
print(misssing_number(ls))