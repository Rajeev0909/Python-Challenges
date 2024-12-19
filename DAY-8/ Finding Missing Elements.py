def missing_elements(list1, list2):
    return list(set(list1) - set(list2))


list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print("Missing Elements:", missing_elements(list1, list2))
