def sort_by_key(lst, key):
    return sorted(lst, key=lambda x: x.get(key))

people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
print("Sorted by age:", sort_by_key(people, "age"))
# Output: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]
