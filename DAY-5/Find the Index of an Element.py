def find_index(lst, element):
    return lst.index(element) if element in lst else -1

# Test the function
data = [10, 20, 30, 40, 50]
print("List =",data)
print("Index of 30:", find_index(data, 30))
print("Index of 60:", find_index(data, 60))
