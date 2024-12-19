di = {
    "a": [1, 2, 3],
    "b": [1, 2],
    "c": [1, 2, 3],
    "d": [1,2,3,4]
}

def validate_keys(di):
    keys = list(di.keys())
    all_values = [set(di[key]) for key in keys]  # Convert all values to sets
    
    # Compare every pair of sets
    for i in range(len(all_values)):
        for j in range(i + 1, len(all_values)):
            if all_values[i] == all_values[j]:
                print(f"Values of keys '{keys[i]}' and '{keys[j]}' are the same.")
            elif all_values[i].issubset(all_values[j]) or all_values[j].issubset(all_values[i]):
                print(f"Values of keys '{keys[i]}' and '{keys[j]}' are subsets.")
            else:
                print(f"Values of keys '{keys[i]}' and '{keys[j]}' are different.")

validate_keys(di)
