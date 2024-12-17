def find_index(tup, element):
    return tup.index(element) if element in tup else -1

# Test the function
my_tuple = (10, 20, 30, 40, 50)
print("Index of 30:", find_index(my_tuple, 30))
print("Index of 60:", find_index(my_tuple, 60))
