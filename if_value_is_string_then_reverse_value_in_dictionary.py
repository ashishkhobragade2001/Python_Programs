di = {"A":123, "B":"python", "C":654}
def if_value_is_string_then_reverse_value(di):
    final_result = {}
    
    for k,v in di.items():
        if isinstance(v, str):
            rev = v[::-1]
            final_result[k] = rev
        else:
            final_result[k] = v
    return final_result
print(if_value_is_string_then_reverse_value(di))