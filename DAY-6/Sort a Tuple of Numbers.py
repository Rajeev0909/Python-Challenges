def sort_tuple(tup, reverse=False):
    return tuple(sorted(tup, reverse=reverse))

# Test the function
numbers = (5, 3, 8, 1, 4)
print("Ascending Order:", sort_tuple(numbers))
print("Descending Order:", sort_tuple(numbers, reverse=True))
