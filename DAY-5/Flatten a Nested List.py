def flatten_list(nested_list):
    flat_list = [item for sublist in nested_list for item in sublist]
    return flat_list

# Test the function
nested = [[1, 2], [3, 4], [5, 6]]
print("Original List",nested)
print("Flattened List:", flatten_list(nested))
