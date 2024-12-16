def find_min_max(lst):
    return min(lst), max(lst)

# Test the function
data = [12, 45, 2, 19, 34, 10]
smallest, largest = find_min_max(data)
print("List =",data)
print("Smallest Number:", smallest)
print("Largest Number:", largest)
