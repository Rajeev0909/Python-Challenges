def max_value_key(d):
    return max(d, key=d.get)

# Test the function
scores = {"Alice": 85, "Bob": 90, "Charlie": 80}
print("Highest Scorer:", max_value_key(scores))
