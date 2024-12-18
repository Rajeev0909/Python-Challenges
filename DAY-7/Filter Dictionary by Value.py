def filter_by_value(d, threshold):
    return {key: value for key, value in d.items() if value >= threshold}

# Test the function
data = {"Alice": 85, "Bob": 60, "Charlie": 70}
print("Filtered Dictionary:", filter_by_value(data, 65))
