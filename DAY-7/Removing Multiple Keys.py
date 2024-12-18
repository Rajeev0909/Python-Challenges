def remove_keys(d, keys_to_remove):
    for key in keys_to_remove:
        d.pop(key, None)  # Use pop with default to avoid errors if the key doesn't exist
    return d

# Test the function
data = {"a": 1, "b": 2, "c": 3, "d": 4}
keys_to_remove = ["b", "d"]
print("After Deletion:", remove_keys(data, keys_to_remove))
