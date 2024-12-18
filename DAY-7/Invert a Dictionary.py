def invert_dictionary(d):
    return {value: key for key, value in d.items()}

# Test the function
data = {"a": 1, "b": 2, "c": 3}
print("Inverted Dictionary:", invert_dictionary(data))
