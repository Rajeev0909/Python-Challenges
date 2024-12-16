def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

# Test the function
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print("List 1",list1)
print("List 2",list2)
print("Common Elements:", find_common_elements(list1, list2))
