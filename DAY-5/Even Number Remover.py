def remove_even(lst):
    return [num for num in lst if num % 2 != 0]

# Test the function
data = [1, 2, 3, 4, 5, 6, 7, 8]
print("List =",data)
print("Odd Numbers Only:", remove_even(data))
