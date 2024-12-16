def split_list(lst):
    mid = len(lst) // 2
    return lst[:mid], lst[mid:]

# Test the function
data = [1, 2, 3, 4, 5, 6]
left, right = split_list(data)
print("Left Half:", left)
print("Right Half:", right)
