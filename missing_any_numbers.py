from collections import Counter

ls = [10,30,40,50,60]

def missing_number(ls):
    miss_number = []
    
    # Function to calculate the most frequent difference
    def differences(ls):
        count = Counter([ls[i] - ls[i - 1] for i in range(1, len(ls))])
        return max(count, key=count.get)  # Return the most frequent difference
    
    difference = differences(ls)  # Get the most frequent difference
    
    for i in range(len(ls) - 1):
        diff = ls[i + 1] - ls[i]
        if diff > difference:  # Check if there's a larger gap than the most frequent difference
            for j in range(1, diff // difference):  # Add missing numbers
                miss_number.append(ls[i] + j * difference)
    
    return miss_number

print("Missing number is:", missing_number(ls))
