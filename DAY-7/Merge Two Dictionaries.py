def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2}

# Test the function
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
print("Merged Dictionary:", merge_dictionaries(dict1, dict2))
