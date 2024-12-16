def rotate_list(lst, n):
    n = n % len(lst)  # Handle rotations larger than the list size
    return lst[-n:] + lst[:-n]

# Test the function
data = [1, 2, 3, 4, 5]
print("Original List",data)
print("Rotated List (2 positions):", rotate_list(data, 2))
