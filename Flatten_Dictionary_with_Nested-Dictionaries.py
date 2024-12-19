def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

d = {
    'a': 1,
    'b': {'c': 2, 'd': {'e': 3}}
}
print("Flattened dictionary:", flatten_dict(d))
# Output: {'a': 1, 'b_c': 2, 'b_d_e': 3}
