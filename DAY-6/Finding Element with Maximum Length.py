def max_length_element(tup):
    return max(tup, key=len)

# Test the function
words = ("Python", "is", "fun", "programming")
print("Longest Word:", max_length_element(words))
