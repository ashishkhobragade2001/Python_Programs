#Data Comparison for ETL Testing

def compare_data(source1, source2):
    mismatches = []
    for row1, row2 in zip(source1, source2):
        if row1 != row2:
            mismatches.append((row1, row2))
    
    if mismatches:
        print("Data mismatches found:")
        for mismatch in mismatches:
            print(f"Source1: {mismatch[0]}, Source2: {mismatch[1]}")
    else:
        print("Data matches in both sources")

# Example usage
data1 = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
data2 = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Charlie"}]

compare_data(data1, data2)
